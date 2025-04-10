import sqlite3
import unittest

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

class TestLogin(unittest.TestCase):  # Add unittest.TestCase inheritance
    def setUp(self):
        # Create the table and add test data before each test
        cursor.execute('''CREATE TABLE IF NOT EXISTS accounts
                         (user TEXT, pass TEXT)''')
        cursor.execute("INSERT INTO accounts VALUES ('admin', 'admin123')")
        conn.commit()

    def tearDown(self):
        # Clean up after each test
        cursor.execute("DROP TABLE IF EXISTS accounts")
        conn.commit()

    def test_basic_auth_check_1(self):  # This method name is correct (starts with "test_")
        result = basic_auth_check('admin', 'admin123')
        self.assertIsNotNone(result, "Authentication should succeed for valid credentials")
        self.assertEqual(result[0], 'admin', "Username should match the input")
        self.assertEqual(result[1], 'admin123', "Password should match the input")

    def test_basic_auth_check_with_sql_injection(self):  # This method name is correct
        result = basic_auth_check("' OR '1'='1", "anypassword")
        self.assertIsNotNone(result, "SQL injection should succeed due to lack of input sanitization")

# Query function that checks login credentials
def basic_auth_check(user_input, pass_input):
    query = f"SELECT * FROM accounts WHERE user = '{user_input}' AND pass = '{pass_input}'"
    print("Running query:", query)
    cursor.execute(query)
    return cursor.fetchone()

if __name__ == '__main__':
    unittest.main()

