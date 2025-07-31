import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, current_user
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.utils import secure_filename
from PIL import Image
import uuid

# Set up logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///victory_rehab.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Upload configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  # type: ignore
login_manager.login_message = 'Please log in to access this page.'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

# Import and register blueprints
from auth import auth as auth_blueprint
from google_auth import google_auth as google_auth_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(google_auth_blueprint)

# Create upload directory
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

with app.app_context():
    import models
    db.create_all()

# Main routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/admissions')
def admissions():
    return render_template('admissions.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        
        # In a real application, you would send this to an email service
        # For now, we'll just flash a success message
        flash('Thank you for your message. We will get back to you soon!', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/gallery')
def gallery():
    from models import GalleryImage
    images = GalleryImage.query.filter_by(approved=True).order_by(GalleryImage.created_at.desc()).all()
    return render_template('gallery.html', images=images)

@app.route('/upload_image', methods=['POST'])
@login_required
def upload_image():
    if 'file' not in request.files:
        flash('No file selected', 'error')
        return redirect(url_for('gallery'))
    
    file = request.files['file']
    caption = request.form.get('caption', '')
    
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('gallery'))
    
    if file and file.filename and allowed_file(file.filename):
        # Generate unique filename
        filename = str(uuid.uuid4()) + '.' + file.filename.rsplit('.', 1)[1].lower()
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Save and resize image
        try:
            image = Image.open(file.stream)
            # Resize if too large
            if image.width > 1200 or image.height > 1200:
                image.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
            image.save(filepath, optimize=True, quality=85)
            
            # Save to database
            from models import GalleryImage
            gallery_image = GalleryImage()
            gallery_image.filename = filename
            gallery_image.caption = caption
            gallery_image.uploaded_by = current_user.id
            gallery_image.approved = False  # Requires admin approval
            db.session.add(gallery_image)
            db.session.commit()
            
            flash('Image uploaded successfully and is pending approval', 'success')
        except Exception as e:
            flash('Error uploading image', 'error')
            logging.error(f"Error uploading image: {e}")
    else:
        flash('Invalid file type. Please upload PNG, JPG, JPEG, GIF, or WebP files.', 'error')
    
    return redirect(url_for('gallery'))

@app.route('/admin')
@login_required
def admin():
    from models import GalleryImage, User
    if not current_user.is_admin:
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    pending_images = GalleryImage.query.filter_by(approved=False).order_by(GalleryImage.created_at.desc()).all()
    approved_images = GalleryImage.query.filter_by(approved=True).order_by(GalleryImage.created_at.desc()).all()
    
    return render_template('admin.html', pending_images=pending_images, approved_images=approved_images)

@app.route('/admin/approve_image/<int:image_id>')
@login_required
def approve_image(image_id):
    from models import GalleryImage
    if not current_user.is_admin:
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    image = GalleryImage.query.get_or_404(image_id)
    image.approved = True
    db.session.commit()
    flash('Image approved successfully', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/delete_image/<int:image_id>')
@login_required
def delete_image(image_id):
    from models import GalleryImage
    if not current_user.is_admin:
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))
    
    image = GalleryImage.query.get_or_404(image_id)
    
    # Delete file from filesystem
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        if os.path.exists(filepath):
            os.remove(filepath)
    except Exception as e:
        logging.error(f"Error deleting file: {e}")
    
    # Delete from database
    db.session.delete(image)
    db.session.commit()
    flash('Image deleted successfully', 'success')
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
