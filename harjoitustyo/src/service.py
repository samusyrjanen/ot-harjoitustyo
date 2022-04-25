class Service:
    def __init__(self, repo):
        self._repository = repo

    def get_estimation(self):
        income = self._repository.read_income()
        expenses = self._repository.read_expenses()
        wealth = self._repository.read_wealth()

        return f'''Tuloarviosi kuukaudessa: {sum(income+expenses)}
Tuloarviosi vuodessa: {12*sum(income+expenses)}

Kokonaisvarallisuutesi kuukauden päästä: {sum(income+expenses) + wealth}
Kokonaisvarallisuutesi vuoden päästä: {12*sum(income+expenses) + wealth}
        '''

    def add_income(self, name, amount):
        self._repository.add_income(amount, name)

    def add_expense(self, name, amount):
        self._repository.add_expense(-amount, name)

    def delete_all_data(self):
        self._repository.clear()

    def print_data(self):
        expenses = self._repository.get_data_expenses()
        income_list = self._repository.get_data_income()
        wealth = self._repository.read_wealth()

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
        self._repository.delete_income(name)

    def delete_expense(self, name):
        self._repository.delete_expense(name)

    def update_wealth(self, wealth):
        self._repository.add_wealth(wealth)
