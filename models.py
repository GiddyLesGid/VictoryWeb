from app import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)  # Original filename
    content_type = db.Column(db.String(50), nullable=False)  # MIME type like 'image/jpeg'
    data = db.Column(db.LargeBinary, nullable=False)  # Binary image data
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('user.id'))  # Optional, can link to User table

    def __repr__(self):
        return f"<Image {self.filename}>"

