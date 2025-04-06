from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os
import subprocess
from config import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'

# Database initialization
def init_db():
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT, content TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('blog.db')
        cursor = conn.cursor()
        # Vulnerable to SQL Injection
        cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
        user = cursor.fetchone()
        conn.close()
        if user:
            return redirect(url_for('index'))
        else:
            return "Login Failed"
    return render_template('login.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = file.filename
        # Vulnerable to Path Traversal
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully'

@app.route('/ping', methods=['POST'])
def ping():
    ip_address = request.form['ip']
    # Vulnerable to Command Injection
    response = subprocess.check_output(f"ping -c 1 {ip_address}", shell=True)
    return response

if __name__ == '__main__':
    app.run(debug=True)
