from app import db, supabase
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)  # stores hash!
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class GalleryImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)  # Stored in Supabase Storage
    caption = db.Column(db.Text)
    filetype = db.Column(db.String(20), default="image")  # "image" or "video"
    uploaded_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    approved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='gallery_items')

    @property
    def public_url(self):
        """Compute the public URL from Supabase only once per request."""
        try:
            return supabase.storage.from_("gallery").get_public_url(self.filename).public_url
        except Exception as e:
            return ""  # fallback to empty string if any error occurs

    def __repr__(self):
        return f"<GalleryItem {self.filename} ({self.filetype})>"

