from flask import Flask, request
import sqlite3

app = Flask(__name__)
app.secret_key = "12345"  # Hardcoded weak secret key

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return '''
        <h2>Login Page</h2>
        <form method="POST" action="/login">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="text" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Vulnerable to SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Executing query:", query)
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        return f"Welcome {username}!"
    else:
        return "Invalid credentials"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
