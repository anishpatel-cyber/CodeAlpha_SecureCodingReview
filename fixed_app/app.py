from flask import Flask, request, render_template_string
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))

DB_NAME = "users.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("SELECT * FROM users WHERE username = ?", ("admin",))
    existing_user = cursor.fetchone()

    if not existing_user:
        hashed_password = generate_password_hash("admin123")
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            ("admin", hashed_password)
        )

    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template_string('''
        <h2>Secure Login Page</h2>
        <form method="POST" action="/login">
            Username: <input type="text" name="username" required><br><br>
            Password: <input type="password" name="password" required><br><br>
            <input type="submit" value="Login">
        </form>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()

    if not username or not password:
        return "Username and password are required.", 400

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Parameterized query prevents SQL injection
    cursor.execute("SELECT username, password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[1], password):
        return f"Welcome {username}!"
    else:
        return "Invalid credentials", 401

if __name__ == '__main__':
    init_db()
    app.run(debug=False)
