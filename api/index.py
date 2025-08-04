from app import app
from vercel_wsgi import handle_wsgi_app

# Entry point for Vercel to serve your Flask app
handler = handle_wsgi_app(app)
