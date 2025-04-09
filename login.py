import sqlite3

# Set up in-memory database and sample data
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("CREATE TABLE accounts (user TEXT, pass TEXT)")
cursor.execute("INSERT INTO accounts VALUES ('admin', 'admin123')")
cursor.execute("INSERT INTO accounts VALUES ('jane', 'janepass')")
conn.commit()

# Query function that checks login credentials
def basic_auth_check(user_input, pass_input):
    query = f"SELECT * FROM accounts WHERE user = '{user_input}' AND pass = '{pass_input}'"
    print("Running query:", query)
    cursor.execute(query)
    return cursor.fetchone()

