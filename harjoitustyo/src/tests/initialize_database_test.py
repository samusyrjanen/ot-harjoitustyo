import unittest
from initialize_database import initialize_database
from file_reader import Repository
from database_connection import get_database_connection

class TestInitialize_database(unittest.TestCase):
    def setUp(self):
        self.file_reader = Repository(get_database_connection())

    def test_initialize_database(self):
        self.file_reader.add_expense(100, 'test', 0)
        initialize_database()
        self.assertEqual(self.file_reader.get_data_expenses(0), [])
