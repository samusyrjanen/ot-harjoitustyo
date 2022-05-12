class Repository:
    '''
    Käsittelee repositorion dataa.

    Attributes:
        conection: Yhteys repositorioon.
    '''

    def __init__(self, connection):
        '''
        Konstruktori, joka tallentaa argumentin muuttujaan.

        Args:
            connection: Yhteys repositorioon.
        '''

        self._connection = connection

    def read_expenses(self, user_id):
        '''
        Hakee repositoriosta kaikki käyttäjän menot.

        Args:
            user_id: Käyttäjän id.

        Returns:
            Lista käyttäjän menoista.
        '''

        cursor = self._connection.cursor()
        sql = 'select amount from expenses where user_id=:user_id'
        cursor.execute(sql, {'user_id':user_id})
        rows = cursor.fetchall()
        return [row['amount'] for row in rows]

    def read_income(self, user_id):
        '''
        Hakee repositoriosta kaikki käyttäjän tulot.

        Args:
            user_id: Käyttäjän id.

        Returns:
            Lista käyttäjän tuloista.
        '''

        cursor = self._connection.cursor()
        sql = 'select amount from income where user_id=:user_id'
        cursor.execute(sql, {'user_id':user_id})
        rows = cursor.fetchall()
        return [row['amount'] for row in rows]

    def read_wealth(self, user_id):
        '''
        Hake repositoriosta käyttäjän varallisuuden.

        Args:
            user_id: Käyttäjän id.

        Returns:
            Käyttäjän varallisuus.
        '''

        cursor = self._connection.cursor()
        sql = 'select amount from wealth where user_id=:user_id order by id desc'
        cursor.execute(sql, {'user_id':user_id})
        result = cursor.fetchone()
        if result:
            return result[0]
        return 0

    def add_expense(self, amount, name, user_id):
        '''
        Lisää menon.

        Args:
            amount: Menon summa.
            name: Menon nimi.
            user_id: Käyttäjän id.
        '''

        cursor = self._connection.cursor()
        sql = 'insert into expenses (amount, name, user_id) values ' \
            '(:amount, :name, :user_id)'
        cursor.execute(sql, {'amount':amount, 'name':name, 'user_id':user_id})
        self._connection.commit()

    def add_income(self, amount, name, user_id):
        '''
        Lisää tulon.

        Args:
            amount: Tulon summa.
            name: Tulon nimi.
            user_id: Käyttäjän id.
        '''

        cursor = self._connection.cursor()
        sql = 'insert into income (amount, name, user_id) values ' \
            '(:amount, :name, :user_id)'
        cursor.execute(sql, {'amount':amount, 'name':name, 'user_id':user_id})
        self._connection.commit()

    def clear(self, user_id):
        '''
        Poistaa tiedot käyttäjästä.

        Args:
            user_id: Käyttäjän id.
        '''

        cursor = self._connection.cursor()
        sql1 = 'delete from expenses where user_id=:user_id'
        sql2 = 'delete from income where user_id=:user_id'
        sql3 = 'delete from wealth where user_id=:user_id'
        cursor.execute(sql1, {'user_id':user_id})
        cursor.execute(sql2, {'user_id':user_id})
        cursor.execute(sql3, {'user_id':user_id})
        self._connection.commit()

    def get_data_expenses(self, user_id):
        '''
        Hakee käyttäjän menojen tiedot.

        Args:
            user_id: Käyttääjän id.

        Returns:
            Lista Käyttäjän menoista ja menojen nimistä.
        '''

        cursor = self._connection.cursor()
        sql = 'select amount, name from expenses where user_id=:user_id'
        cursor.execute(sql, {'user_id':user_id})
        rows = cursor.fetchall()
        return [(row['amount'], row['name']) for row in rows]

    def get_data_income(self, user_id):
        '''
        Hakee käyttäjän tulojen tiedot.

        Args:
            user_id: Käyttääjän id.

        Returns:
            Lista Käyttäjän tuloista ja tulojen nimistä.
        '''

        cursor = self._connection.cursor()
        sql = 'select amount, name from income where user_id=:user_id'
        cursor.execute(sql, {'user_id':user_id})
        rows = cursor.fetchall()
        return [(row['amount'], row['name']) for row in rows]

    def delete_income(self, name, user_id):
        '''
        Poistaa yksittäisen tulon.

        Args:
            name: Tulon nimi.
            user_id: Käyttäjän id.
        '''

        cursor = self._connection.cursor()
        sql = 'delete from income where name=:name and user_id=:user_id'
        cursor.execute(sql, {'name':name, 'user_id':user_id})
        self._connection.commit()

    def delete_expense(self, name, user_id):
        '''
        Poistaa yksittäisen menon.

        Args:
            name: Menon nimi.
            user_id: Käyttäjän id.
        '''

        cursor = self._connection.cursor()
        sql = 'delete from expenses where name=:name and user_id=:user_id'
        cursor.execute(sql, {'name':name, 'user_id':user_id})
        self._connection.commit()

    def add_wealth(self, wealth, user_id):
        '''
        Päivittää käyttäjän tämänhetkisen varallisuuden.

        Args:
            wealth: Varallisuus
            user_id: Käyttäjän id.
        '''

        cursor = self._connection.cursor()
        sql = 'insert into wealth (amount, user_id) values (:wealth, :user_id)'
        cursor.execute(sql, {'wealth':wealth, 'user_id':user_id})
        self._connection.commit()

    def register(self, username, password):
        '''
        Lisää uuden käyttäjän tietokantaan.

        Args:
            username: Käyttäjätunnus.
            password: Salasanan sha256 -muoto.

        Returns:
            True jos rekisteröityminen ja kirjautuminen onnistuu, muutoin False.
        '''

        cursor = self._connection.cursor()
        try:
            sql = 'insert into users (username, password) ' \
                'values (:username, :password)'
            cursor.execute(sql, {'username':username, 'password':password})
            self._connection.commit()
        except:
            return False
        return self.login(username, password)

    def login(self, username, password):
        '''
        Hakee käyttäjän tietokannasta.

        Args:
            username: Käyttäjätunnus
            password: Salasanan sha256 -muoto.

        Returns:
            True jos kirjautuminen onnistuu, muutoin False.
        '''

        cursor = self._connection.cursor()
        sql = 'select password from users where username=:username'
        result = cursor.execute(sql, {'username':username})
        try:
            right_password = result.fetchone()[0]
        except TypeError:
            return False
        return password == right_password

    def user_id(self, username):
        '''
        Hakee käyttäjän id:n.

        args:
            username: Käyttäjätunnus

        returns:
            id
        '''

        cursor = self._connection.cursor()
        sql = 'select id from users where username=:username'
        result = cursor.execute(sql, {'username':username})
        return result.fetchone()[0]

    def delete_user(self, username):
        '''
        Poistaa käyttäjän tietokannasta.

        Args:
            username: Käyttäjänimi.
        '''

        cursor = self._connection.cursor()
        sql = 'delete from users where username=:username'
        cursor.execute(sql, {'username':username})
        self._connection.commit()

    def check_username_availability(self, username):
        '''
        Tarkistaa onko käyttäjätunnus vapaa.

        Args:
            username: Tarkistettava käyttäjätunnus

        Returns:
            True jos käyttäjätunnus on vapaa, False jos varattu.
        '''

        cursor = self._connection.cursor()
        sql = 'select username from users where username=:username'
        result = cursor.execute(sql, {'username':username})
        if result.fetchone():
            return False
        return True

    def search_income(self, name, user_id):
        '''
        Etsii tulon nimen perusteella.

        Args:
            name: tulon nimi

        Returns:
            True jos kyseinen tulo löytyy, muutoin False.
        '''

        cursor = self._connection.cursor()
        sql = 'select name from income where name=:name and user_id=:user_id'
        result = cursor.execute(sql, {'name':name, 'user_id':user_id})
        if result.fetchone():
            return True
        return False

    def search_expense(self, name, user_id):
        '''
        Etsii menon nimen perusteella.

        Args:
            name: menon nimi

        Returns:
            True jos kyseinen meno löytyy, muutoin False.
        '''

        cursor = self._connection.cursor()
        sql = 'select name from expenses where name=:name and user_id=:user_id'
        result = cursor.execute(sql, {'name':name, 'user_id':user_id})
        if result.fetchone():
            return True
        return False