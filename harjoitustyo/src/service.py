import hashlib

class Service:
    def __init__(self, repo):
        self._repository = repo
        self._user = None
        self._user_id = None

    def get_estimation(self):
        income = self._repository.read_income(self._user_id)
        expenses = self._repository.read_expenses(self._user_id)
        wealth = self._repository.read_wealth(self._user_id)

        return f'''Tuloarviosi kuukaudessa: {sum(income+expenses)}
Tuloarviosi vuodessa: {12*sum(income+expenses)}

Kokonaisvarallisuutesi kuukauden päästä: {sum(income+expenses) + wealth}
Kokonaisvarallisuutesi vuoden päästä: {12*sum(income+expenses) + wealth}'''

    def add_income(self, name, amount):
        self._repository.add_income(amount, name, self._user_id)

    def add_expense(self, name, amount):
        self._repository.add_expense(-amount, name, self._user_id)

    def delete_all_data(self):
        self._repository.clear(self._user_id)

    def print_data(self):
        expenses = self._repository.get_data_expenses(self._user_id)
        income_list = self._repository.get_data_income(self._user_id)
        wealth = self._repository.read_wealth(self._user_id)

        print_income = 'Tulot kuukaudessa:\n'
        print_expenses = 'Menot kuukaudessa:\n'
        for income in income_list:
            print_income += f'{income[0]} {income[1]}\n'
        print_income += '\n'

        for expense in expenses:
            print_expenses += f'{expense[0]} {expense[1]}\n'
        print_expenses += '\n'

        print_wealth = f'Tämänhetkinen varallisuutesi:\n{wealth}\n'

        return print_income + print_expenses + print_wealth

    def delete_income(self, name):
        self._repository.delete_income(name, self._user_id)

    def delete_expense(self, name):
        self._repository.delete_expense(name, self._user_id)

    def update_wealth(self, wealth):
        self._repository.add_wealth(wealth, self._user_id)

    def register(self, username, password):
        hash_value = hashlib.sha256(password.encode('utf-8')).hexdigest()

        if self._repository.register(username, hash_value):
            self._user = username
            self._user_id = self._repository.user_id(username)
            return True
        return False

    def login(self, username, password):
        hash_value = hashlib.sha256(password.encode('utf-8')).hexdigest()

        if self._repository.login(username, hash_value):
            self._user = username
            self._user_id = self._repository.user_id(username)
            return True
        return False

    def logout(self):
        self._user = None
        self._user_id = None

    def username(self):
        return self._user
