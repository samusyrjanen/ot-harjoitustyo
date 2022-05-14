import unittest
from initialize_database import initialize_database
from service import Service
from file_reader import Repository
from database_connection import get_database_connection

class TestService(unittest.TestCase):
    def setUp(self):
        initialize_database()
        repository = Repository(get_database_connection())
        self.service = Service(repository)
        self.service.register('user', 'password')

    def test_get_estimation(self):
        self.service.add_expense('expense', 1)
        self.service.add_income('income', 2)
        self.service.update_wealth(10)
        self.assertEqual(self.service.get_estimation(), '''Tuloarviosi kuukaudessa: 1
Tuloarviosi vuodessa: 12

Kokonaisvarallisuutesi kuukauden päästä: 11
Kokonaisvarallisuutesi vuoden päästä: 22
            ''')

    def test_register(self):
        self.assertEqual(self.service.register('TestUser', 'password'), True)

    def test_login(self):
        self.assertEqual(self.service.login('user', 'password'), True)

    def test_username(self):
        self.assertEqual(self.service.username(), 'user')
    
    def test_logout(self):
        self.service.logout()
        self.assertEqual(self.service.username(), None)