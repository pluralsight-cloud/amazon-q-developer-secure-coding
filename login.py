import sqlite3

# Set up a sample in-memory database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create a simple users table
cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES ('admin', 'admin123')")
cursor.execute("INSERT INTO users VALUES ('john', 'johnspassword')")
conn.commit()

# Insecure login function
def insecure_login(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Executing query:", query)
    cursor.execute(query)
    return cursor.fetchone()

# Try normal login
print("Normal login:")
print(insecure_login('john', 'johnspassword'))  # Should succeed

# Try SQL injection
print("\nSQL injection login:")
print(insecure_login("john' --", 'wrongpassword'))  # Bypasses password check
