import hashlib

class Service:
    '''
    Huolehtii sovelluslogiikasta ja käyttöliittymän ja repositorion kommunikaatiosta.

    Attributes:
        repo: Luokka, joka käsittelee dataa.
    '''

    def __init__(self, repo):
        '''
        Konstruktori, joka luo muuttujat.

        Args:
            repo: Luokka, joka käsittelee dataa.
        '''

        self._repository = repo
        self._user = None
        self._user_id = None

    def get_estimation(self):
        '''
        Luo datan perusteella arvion varallisuuden kehityksestä.

        Returns:
            Arvio tekstinä.
        '''

        income = self._repository.read_income(self._user_id)
        expenses = self._repository.read_expenses(self._user_id)
        wealth = self._repository.read_wealth(self._user_id)

        return f'''Tuloarviosi kuukaudessa: {sum(income+expenses)}
Tuloarviosi vuodessa: {12*sum(income+expenses)}

Kokonaisvarallisuutesi kuukauden päästä: {sum(income+expenses) + wealth}
Kokonaisvarallisuutesi vuoden päästä: {12*sum(income+expenses) + wealth}'''

    def add_income(self, name, amount):
        '''
        Lisää kuukausittaisen tulon.

        Args:
            name: Tulon nimi.
            amount: Tulon summa.
        '''

        self._repository.add_income(amount, name, self._user_id)

    def add_expense(self, name, amount):
        '''
        Lisää kuukausittaisen menon.

        Args:
            name: Menon nimi.
            amount: Menon summa.
        '''

        self._repository.add_expense(-amount, name, self._user_id)

    def delete_all_data(self):
        '''
        Poistaa kaiken datan käyttäjästä.
        '''

        self._repository.clear(self._user_id)

    def print_data(self):
        '''
        Näyttää annetun datan.

        Returns:
            Data tekstinä.
        '''

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
        '''
        Poistaa tietyn tulon.

        Args:
            name: Poistettavan tulon nimi.
        '''

        self._repository.delete_income(name, self._user_id)

    def delete_expense(self, name):
        '''
        Poistaa tietyn menon.

        Args:
            name: Poistettavan menon nimi.
        '''

        self._repository.delete_expense(name, self._user_id)

    def update_wealth(self, wealth):
        '''
        Päivittää repositorioon tämänhetkisen varallisuuden.

        Args:
            wealth: Varallisuuden määrä.
        '''

        self._repository.add_wealth(wealth, self._user_id)

    def register(self, username, password):
        '''
        Rekisteröi uuden käyttäjän.

        Args:
            username: Käyttäjätunnus
            password: Salasana

        Returns:
            True jos rekisteröityminen ja kirjautuminen onnistuu, muussa tapauksessa False.
        '''

        hash_value = hashlib.sha256(password.encode('utf-8')).hexdigest()

        if self._repository.register(username, hash_value):
            self._user = username
            self._user_id = self._repository.user_id(username)
            return True
        return False

    def login(self, username, password):
        '''
        Kirjautuu sisään olemassa olevalla käyttäjällä.

        Args:
            username: Käyttäjätunnus
            password: Salasana

        Returns:
            True jos kirjautuminen onnistuu, muussa tapauksessa False.
        '''

        hash_value = hashlib.sha256(password.encode('utf-8')).hexdigest()

        if self._repository.login(username, hash_value):
            self._user = username
            self._user_id = self._repository.user_id(username)
            return True
        return False

    def logout(self):
        '''
        Kirjautuu ulos.
        '''

        self._user = None
        self._user_id = None

    def username(self):
        '''
        Returns:
            Käyttäjätunnus, jos kirjautuneena, muussa tapauksessa None.
        '''

        return self._user

    def check_username_availability(self, username):
        '''
        Tarkistaa onko käyttäjänimi vapaa.

        Args:
            username: Tarkistettava käyttäjätunnus

        Returns:
            True jos vapaa, muussa tapauksessa false.
        '''

        return self._repository.check_username_availability(username)

    def search_income(self, name):
        '''
        Etsii tulon nimen perusteella.

        Args:
            name: tulon nimi

        Returns:
            True jos kyseinen tulo löytyy, muutoin False.
        '''

        return self._repository.search_income(name, self._user_id)

    def search_expense(self, name):
        '''
        Etsii menon nimen perusteella.

        Args:
            name: menon nimi

        Returns:
            True jos kyseinen meno löytyy, muutoin False.
        '''

        return self._repository.search_expense(name, self._user_id)