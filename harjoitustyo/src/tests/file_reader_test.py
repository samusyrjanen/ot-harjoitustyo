import unittest
from file_reader import Repository
from database_connection import get_database_connection
from initialize_database import initialize_database

class TestRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.file_reader = Repository(get_database_connection())
    
    def test_read_expenses(self):
        self.assertEqual(self.file_reader.read_expenses(0), [])

    def test_read_income(self):
        self.assertEqual(self.file_reader.read_income(0), [])

    def test_add_expense(self):
        self.file_reader.add_expense(-10, 'test1', 0)
        self.file_reader.add_expense(-20, 'test2', 0)
        self.assertEqual(self.file_reader.read_expenses(0), [-10, -20])

    def test_add_income(self):
        self.file_reader.add_income(10, 'test3', 0)
        self.file_reader.add_income(20, 'test4', 0)
        self.assertEqual(self.file_reader.read_income(0), [10, 20])

    def test_add_wealth(self):
        self.file_reader.add_wealth(2000, 0)
        self.assertEqual(self.file_reader.read_wealth(0), 2000)

    def test_get_data_expenses(self):
        self.file_reader.add_expense(-10, 'test1', 0)
        self.file_reader.add_expense(-20, 'test2', 0)
        self.assertEqual(self.file_reader.get_data_expenses(0), [(-10, 'test1'), (-20, 'test2')])

    def test_get_data_income(self):
        self.file_reader.add_income(10, 'test3', 0)
        self.file_reader.add_income(20, 'test4', 0)
        self.assertEqual(self.file_reader.get_data_income(0), [(10, 'test3'), (20, 'test4')])

    def test_delete_income(self):
        self.file_reader.add_income(10, 'test3', 0)
        self.file_reader.add_income(20, 'test4', 0)
        self.file_reader.delete_income('test3', 0)
        self.assertEqual(self.file_reader.get_data_income(0), [(20, 'test4')])

    def test_delete_expense(self):
        self.file_reader.add_expense(-10, 'test1', 0)
        self.file_reader.add_expense(-20, 'test2', 0)
        self.file_reader.delete_expense('test1', 0)
        self.assertEqual(self.file_reader.get_data_expenses(0), [(-20, 'test2')])

    def test_clear(self):
        self.file_reader.add_expense(-10, 'test1', 0)
        self.file_reader.add_income(10, 'test3', 0)
        self.file_reader.add_wealth(2000, 0)
        self.file_reader.clear(0)
        self.assertEqual(self.file_reader.read_expenses(0), [])
        self.assertEqual(self.file_reader.read_income(0), [])
        self.assertEqual(self.file_reader.read_wealth(0), 0)

    def test_register(self):
        self.assertEqual(self.file_reader.register('FB4BBB7E5597EC7740CDE22B835A8189C1461CB2F3CFD142DDCDB7B591F70A6D', 'password'), True)
        self.assertEqual(self.file_reader.register('FB4BBB7E5597EC7740CDE22B835A8189C1461CB2F3CFD142DDCDB7B591F70A6D', 'password'), False)

    def test_login(self):
        self.file_reader.register('FB4BBB7E5597EC7740CDE22B835A8189C1461CB2F3CFD142DDCDB7B591F70A6D', 'password')
        self.assertEqual(self.file_reader.login('FB4BBB7E5597EC7740CDE22B835A8189C1461CB2F3CFD142DDCDB7B591F70A6D', 'password'), True)
        self.assertEqual(self.file_reader.login('FB4BBB7E5597EC7740CDE22B835A8189C1461CB2F3CFD142DDCDB7B591F70A6D', 'p'), False)

    def test_user_id(self):
        self.file_reader.register('FB4BBB7E5597EC7740CDE22B835A8189C1461CB2F3CFD142DDCDB7B591F70A6D', 'password')
        self.assertEqual(self.file_reader.user_id('FB4BBB7E5597EC7740CDE22B835A8189C1461CB2F3CFD142DDCDB7B591F70A6D'), 1)

    def test_delete_user(self):
        self.file_reader.register('FB4BBB7E5597EC7740CDE22B835A8189C1461CB2F3CFD142DDCDB7B591F70A6D', 'password')
        self.file_reader.delete_user('FB4BBB7E5597EC7740CDE22B835A8189C1461CB2F3CFD142DDCDB7B591F70A6D')
        self.assertEqual(self.file_reader.login('FB4BBB7E5597EC7740CDE22B835A8189C1461CB2F3CFD142DDCDB7B591F70A6D', 'password'), False)
