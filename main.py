from app import app
from vercel_wsgi import handle_wsgi_app

# Export a WSGI handler as expected by Vercel
handler = handle_wsgi_app(app)

