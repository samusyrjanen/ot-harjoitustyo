import unittest
from file_reader import Repository
from database_connection import get_database_connection

class TestRepository(unittest.TestCase):
    def setUp(self):
        self.file_reader = Repository(get_database_connection())
        self.file_reader.clear()
    
    def test_read_expenses(self):
        self.assertEqual(self.file_reader.read_expenses(), [])

    def test_read_income(self):
        self.assertEqual(self.file_reader.read_income(), [])

    def test_add_expense(self):
        self.file_reader.add_expense(-10, 'test1')
        self.file_reader.add_expense(-20, 'test2')
        self.assertEqual(self.file_reader.read_expenses(), [-10, -20])

    def test_add_income(self):
        self.file_reader.add_income(10, 'test3')
        self.file_reader.add_income(20, 'test4')
        self.assertEqual(self.file_reader.read_income(), [10, 20])

    def test_add_wealth(self):
        self.file_reader.add_wealth(2000)
        self.assertEqual(self.file_reader.read_wealth(), 2000)

    def test_get_data_expenses(self):
        self.file_reader.add_expense(-10, 'test1')
        self.file_reader.add_expense(-20, 'test2')
        self.assertEqual(self.file_reader.get_data_expenses(), [(-10, 'test1'), (-20, 'test2')])

    def test_get_data_income(self):
        self.file_reader.add_income(10, 'test3')
        self.file_reader.add_income(20, 'test4')
        self.assertEqual(self.file_reader.get_data_income(), [(10, 'test3'), (20, 'test4')])

    def test_delete_income(self):
        self.file_reader.add_income(10, 'test3')
        self.file_reader.add_income(20, 'test4')
        self.file_reader.delete_income('test3')
        self.assertEqual(self.file_reader.get_data_income(), [(20, 'test4')])

    def test_delete_expense(self):
        self.file_reader.add_expense(-10, 'test1')
        self.file_reader.add_expense(-20, 'test2')
        self.file_reader.delete_expense('test1')
        self.assertEqual(self.file_reader.get_data_expenses(), [(-20, 'test2')])

    def test_clear(self):
        self.file_reader.add_expense(-10, 'test1')
        self.file_reader.add_income(10, 'test3')
        self.file_reader.add_wealth(2000)
        self.file_reader.clear()
        self.assertEqual(self.file_reader.read_expenses(), [])
        self.assertEqual(self.file_reader.read_income(), [])
        self.assertEqual(self.file_reader.read_wealth(), 0)
