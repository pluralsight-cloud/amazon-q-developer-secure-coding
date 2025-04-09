import sqlite3

# Set up a sample in-memory database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create a simple credentials table
cursor.execute("CREATE TABLE accounts (user TEXT, pass TEXT)")
cursor.execute("INSERT INTO accounts VALUES ('admin', 'admin123')")
cursor.execute("INSERT INTO accounts VALUES ('alice', 'alicepass')")
conn.commit()

# Function that queries for matching user credentials
def check_credentials(user_input, pass_input):
    query = f"SELECT * FROM accounts WHERE user = '{user_input}' AND pass = '{pass_input}'"
    print("Executing query:", query)
    cursor.execute(query)
    return cursor.fetchone()

# Example of a successful login
print("Valid login attempt:")
print(check_credentials('alice', 'alicepass'))  # Should succeed

# Example of an unexpected login result
print("\nUnexpected login attempt:")
print(check_credentials("alice' --", 'wrongpass'))  # May bypass password check if not protected
