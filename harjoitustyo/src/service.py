'''from file_reader import Repository
from database_connection import get_database_connection

commands = {
    'x': 'x lopeta',
    '0': '0 ohje',
    '1': '1 lisaa tulo',
    '2': '2 lisaa meno',
    '3': '3 tulosta arvio',
    '4': '4 tulosta kaikki menot ja tulot',
    '5': '5 poista tulo',
    '6': '6 poista meno',
    '7': '7 lisaa tämänhetkinen varallisuus',
    '8': '8 poista kaikki tiedot'
}

class UI:
    def __init__(self, service):
        self._service = service

    def help(self):
        for command in commands.values():
            print(command)
        print()

    def start(self):
        self.help()

        while True:
            command = input('anna komento: ')
            print()

            if command not in commands:
                print('virheellinen komento')
                self.help()
                continue

            if command == 'x':
                break
            if command == '0':
                self.help()
            if command == '1':
                self._add_income()
            if command == '2':
                self._add_expense()
            if command == '3':
                self._print_estimation()
            if command == '4':
                self._print_data()
            if command == '5':
                self._delete_income()
            if command == '6':
                self._delete_expense()
            if command == '7':
                self._update_wealth()
            if command == '8':
                self._delete_all_data()

    def _add_income(self):
        name = input('Anna nimi tulolle: ')
        amount = int(input('Tulon määrä euroina: '))
        print()

        self._service.add_income(amount, name)

    def _add_expense(self):
        name = input('Anna nimi maksulle: ')
        amount = int(input('Maksujen määrä euroina: '))
        print()

        self._service.add_expense(-amount, name)

    def _print_estimation(self):
        income = self._service.read_income()
        expenses = self._service.read_expenses()
        wealth = self._service.read_wealth()

        print(f''''''Tuloarviosi kuukaudessa: {sum(income+expenses)}##############
Tuloarviosi vuodessa: {12*sum(income+expenses)}

Varallisuutesi kuukauden päästä: {sum(income+expenses) + wealth}
Varallisuutesi vuoden päästä: {12*sum(income+expenses) + wealth}
        '''''')##################

    def _delete_all_data(self):
        self._service.clear()
        print('Tiedot poistettu')
        print()

    def _print_data(self):
        expenses = self._service.get_data_expenses()
        income_list = self._service.get_data_income()

        print('Tulot:')
        for income in income_list:
            print(income[0], income[1])
        print()

        print('Menot:')
        for expense in expenses:
            print(expense[0], expense[1])
        print()

    def _delete_income(self):
        name = input('Anna poistettavan tulon nimi: ')
        print()

        self._service.delete_income(name)

    def _delete_expense(self):
        name = input('Anna poistettavan menon nimi: ')
        print()

        self._service.delete_expense(name)

    def _update_wealth(self):
        wealth = int(input('Anna tämänhetkinen varallisuus: '))
        print()

        self._service.add_wealth(wealth)

repository = Repository(get_database_connection())
sovellus = UI(repository)
sovellus.start()
'''

from file_reader import Repository
from database_connection import get_database_connection

class Service:
    def __init__(self, repository):
        self._repository = repository

    def _get_estimation(self):
        income = self._repository.read_income()
        expenses = self._repository.read_expenses()
        wealth = self._repository.read_wealth()

        return f'''Tuloarviosi kuukaudessa: {sum(income+expenses)}
Tuloarviosi vuodessa: {12*sum(income+expenses)}

Varallisuutesi kuukauden päästä: {sum(income+expenses) + wealth}
Varallisuutesi vuoden päästä: {12*sum(income+expenses) + wealth}
        '''

    def _add_income(self, name, amount):
        self._repository.add_income(amount, name)

    def _add_expense(self, name, amount):
        self._repository.add_expense(-amount, name)

    def _delete_all_data(self):
        self._repository.clear()

    def _print_data(self):
        expenses = self._repository.get_data_expenses()
        income_list = self._repository.get_data_income()

        print_income = 'Tulot:\n'
        print_expenses = 'Menot:\n'
        for income in income_list:
            print_income += f'{income[0]} {income[1]}\n'
        print_income += '\n'

        for expense in expenses:
            print_expenses += f'{expense[0]} {expense[1]}\n'
        print_expenses += '\n'

        return print_income + print_expenses

    def _delete_income(self, name):
        self._repository.delete_income(name)

    def _delete_expense(self, name):
        self._repository.delete_expense(name)

    def _update_wealth(self):
        wealth = int(input('Anna tämänhetkinen varallisuus: '))

        self._repository.add_wealth(wealth)

repository = Repository(get_database_connection())
service = Service(repository)