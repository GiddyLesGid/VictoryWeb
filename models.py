from app import db, supabase
from flask_login import UserMixin
from datetime import datetime

# --- User model ---
class User(UserMixin, db.Model):
    __tablename__ = 'user'  # explicitly set table name (reserved word!)
    __table_args__ = {'schema': 'public'}  # Supabase default schema

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)  # hashed password
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.username}>"


# --- GalleryImage model ---
class GalleryImage(db.Model):
    __tablename__ = 'gallery_image'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)  # Supabase storage
    caption = db.Column(db.Text)
    filetype = db.Column(db.String(20), default="image")  # image or video
    uploaded_by = db.Column(db.Integer, db.ForeignKey('public.user.id'))  # note schema prefix
    approved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='gallery_items')

    @property
    def public_url(self):
        """Compute the public URL from Supabase."""
        try:
            return supabase.storage.from_("gallery").get_public_url(self.filename).public_url
        except Exception:
            return ""

    def __repr__(self):
        return f"<GalleryImage {self.filename} ({self.filetype})>"

