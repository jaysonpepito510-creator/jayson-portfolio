import os
from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "jayson-portfolio-secret-200316")

# Database configuration supporting PostgreSQL on production & SQLite in /tmp on Vercel serverless
database_url = os.environ.get("DATABASE_URL")
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

if not database_url:
    # Vercel serverless filesystem is read-only except for /tmp
    db_path = os.path.join('/tmp', 'portfolio.db')
    database_url = f'sqlite:///{db_path}'

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)