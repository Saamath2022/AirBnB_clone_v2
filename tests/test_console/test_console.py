import unittest
import MySQLdb
from ..console import HBNBCommand
from io import StringIO
import sys

class TestCreateState(unittest.TestCase):
    def setUp(self):
        # Connect to the database
        self.db = MySQLdb.connect(
            host="localhost",
            user="hbnb_test_user",
            passwd="hbnb_test_pwd",
            db="hbnb_test_db"
        )
        self.cursor = self.db.cursor()
    
    def tearDown(self):
        # Close the database connection
        self.cursor.close()
        self.db.close()

    def get_state_count(self):
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        count = self.cursor.fetchone()[0]
        return count
    
    def test_create_state(self):
        # Get initial count of records in the states table
        initial_count = self.get_state_count()
        
        # Run the console command to create a new state
        console_output = StringIO()
        sys.stdout = console_output
        HBNBCommand().onecmd('create State name="California"')
        sys.stdout = sys.__stdout__
        
        # Get the new count of records in the states table
        new_count = self.get_state_count()
        
        # Check if the count increased by 1
        self.assertEqual(new_count, initial_count + 1)

if __name__ == '__main__':
    unittest.main()

