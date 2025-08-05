from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return "Victory Rehabilitation Centre"

@app.route('/dbtest')
def dbtest():
    try:
        conn = psycopg2.connect(
            host=os.getenv("PGHOST"),
            user=os.getenv("PGUSER"),
            password=os.getenv("PGPASSWORD"),
            dbname=os.getenv("PGDATABASE"),
            port=os.getenv("PGPORT")
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()
        return f"Database connected successfully: {result}"
    except Exception as e:
        return f"Database connection failed: {e}"
