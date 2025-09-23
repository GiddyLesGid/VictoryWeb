import os
import logging
import uuid
from flask import (
    Flask, render_template, request, redirect, url_for, flash, send_from_directory
)
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, current_user
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import NullPool
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_migrate import Migrate
from supabase import create_client

logging.basicConfig(level=logging.DEBUG)

# --- SQLAlchemy setup ---
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# --- Database Config ---
database_url = os.environ.get("DATABASE_URL")
if not database_url:
    raise RuntimeError("DATABASE_URL is not set — check your Vercel environment variables!")

# For serverless (Vercel), always use NullPool so no connections are held between requests
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "poolclass": NullPool
}
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB limit

migrate = Migrate(app, db)

# --- Supabase setup ---
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'mp4', 'mov', 'avi'}

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'

from models import User, GalleryImage


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))


# --- Blueprints ---
from auth import auth as auth_blueprint
from google_auth import google_auth as google_auth_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(google_auth_blueprint)


# --- Routes ---
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
        flash('Thank you for your message. We will get back to you soon!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')


@app.route('/gallery')
def gallery():
    items = GalleryImage.query.filter_by(approved=True).order_by(GalleryImage.created_at.desc()).all()
    return render_template('gallery.html', items=items)


@app.route('/upload_media', methods=['POST'])
@login_required
def upload_media():
    if 'file' not in request.files:
        flash('No file selected', 'error')
        return redirect(url_for('gallery'))

    file = request.files['file']
    caption = request.form.get('caption', '')

    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('gallery'))

    if file and allowed_file(file.filename):
        ext = file.filename.rsplit('.', 1)[1].lower()
        filename = f"{uuid.uuid4()}.{ext}"

        # Detect file type
        mimetype = file.mimetype
        if mimetype.startswith("image/"):
            filetype = "image"
        elif mimetype.startswith("video/"):
            filetype = "video"
        else:
            flash('Unsupported file type', 'error')
            return redirect(url_for('gallery'))

        try:
            # Upload to Supabase storage bucket "gallery"
            supabase.storage.from_("gallery").upload(filename, file)

            gallery_item = GalleryImage(
                filename=filename,
                caption=caption,
                uploaded_by=current_user.id,
                approved=False,
                filetype=filetype
            )
            db.session.add(gallery_item)
            db.session.commit()

            flash(f'{filetype.capitalize()} uploaded successfully and pending approval', 'success')

        except Exception as e:
            logging.error(f"Error uploading media: {e}")
            flash(f'Error uploading media: {str(e)}', 'error')

    else:
        flash('Invalid file type. Allowed: png, jpg, jpeg, gif, webp, mp4, mov, avi', 'error')

    return redirect(url_for('gallery'))


@app.route('/media/<filename>')
def get_media(filename):
    # Generate a public URL from Supabase storage
    url = supabase.storage.from_("gallery").get_public_url(filename)
    return redirect(url)


@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))

    pending = GalleryImage.query.filter_by(approved=False).order_by(GalleryImage.created_at.desc()).all()
    approved = GalleryImage.query.filter_by(approved=True).order_by(GalleryImage.created_at.desc()).all()

    return render_template('admin.html', pending_images=pending, approved_images=approved)


@app.route('/admin/approve_image/<int:image_id>')
@login_required
def approve_image(image_id):
    if not current_user.is_admin:
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))

    image = GalleryImage.query.get_or_404(image_id)
    image.approved = True
    db.session.commit()
    flash('Media approved successfully', 'success')
    return redirect(url_for('admin'))


@app.route('/admin/delete_image/<int:image_id>')
@login_required
def delete_image(image_id):
    if not current_user.is_admin:
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('index'))

    image = GalleryImage.query.get_or_404(image_id)
    db.session.delete(image)
    db.session.commit()
    flash('Media deleted successfully', 'success')
    return redirect(url_for('admin'))


@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, 'robots.txt')


@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

