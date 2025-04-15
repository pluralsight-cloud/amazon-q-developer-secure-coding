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

    def test_basic_auth_check_valid_credentials(self):
        """
        Test that basic_auth_check returns a valid result for correct credentials.
        """
        result = basic_auth_check('admin', 'admin123')
        self.assertIsNotNone(result)
        self.assertEqual(result, ('admin', 'admin123'))

# Query function that checks login credentials
def basic_auth_check(user_input, pass_input):
    query = f"SELECT * FROM accounts WHERE user = '{user_input}' AND pass = '{pass_input}'"
    print("Running query:", query)
    cursor.execute(query)
    return cursor.fetchone()

if __name__ == '__main__':
    unittest.main()



def test_basic_auth_check_with_sql_injection(self):
    """
    Test the basic_auth_check function with a SQL injection attempt.
    This test verifies that the function is vulnerable to SQL injection,
    which is an unhandled edge case in the current implementation.
    """
    # SQL injection attempt
    malicious_input = "' OR '1'='1"
    result = basic_auth_check(malicious_input, "anypassword")

    # The function is vulnerable if it returns a result
    self.assertIsNotNone(result, "The function is vulnerable to SQL injection")
