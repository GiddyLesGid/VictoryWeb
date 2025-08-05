from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return "Victory Rehabilitation Centre"

# No need for handle_wsgi_app or vercel-wsgi
