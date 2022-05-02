class Repository:
    def __init__(self, connection):
        self._connection = connection

    def read_expenses(self, user_id):
        cursor = self._connection.cursor()
        sql = 'select amount from expenses where user_id=:user_id'
        cursor.execute(sql, {'user_id':user_id})
        rows = cursor.fetchall()
        return [row['amount'] for row in rows]

    def read_income(self, user_id):
        cursor = self._connection.cursor()
        sql = 'select amount from income where user_id=:user_id'
        cursor.execute(sql, {'user_id':user_id})
        rows = cursor.fetchall()
        return [row['amount'] for row in rows]

    def read_wealth(self, user_id):
        cursor = self._connection.cursor()
        sql = 'select amount from wealth where user_id=:user_id order by id desc'
        cursor.execute(sql, {'user_id':user_id})
        result = cursor.fetchone()
        if result:
            return result[0]
        return 0

    def add_expense(self, amount, name, user_id):
        cursor = self._connection.cursor()
        sql = 'insert into expenses (amount, name, user_id) values ' \
            '(:amount, :name, :user_id)'
        cursor.execute(sql, {'amount':amount, 'name':name, 'user_id':user_id})
        self._connection.commit()

    def add_income(self, amount, name, user_id):
        cursor = self._connection.cursor()
        sql = 'insert into income (amount, name, user_id) values ' \
            '(:amount, :name, :user_id)'
        cursor.execute(sql, {'amount':amount, 'name':name, 'user_id':user_id})
        self._connection.commit()

    def clear(self, user_id):
        cursor = self._connection.cursor()
        sql1 = 'delete from expenses where user_id=:user_id'
        sql2 = 'delete from income where user_id=:user_id'
        sql3 = 'delete from wealth where user_id=:user_id'
        cursor.execute(sql1, {'user_id':user_id})
        cursor.execute(sql2, {'user_id':user_id})
        cursor.execute(sql3, {'user_id':user_id})
        self._connection.commit()

    def get_data_expenses(self, user_id):
        cursor = self._connection.cursor()
        sql = 'select amount, name from expenses where user_id=:user_id'
        cursor.execute(sql, {'user_id':user_id})
        rows = cursor.fetchall()
        return [(row['amount'], row['name']) for row in rows]

    def get_data_income(self, user_id):
        cursor = self._connection.cursor()
        sql = 'select amount, name from income where user_id=:user_id'
        cursor.execute(sql, {'user_id':user_id})
        rows = cursor.fetchall()
        return [(row['amount'], row['name']) for row in rows]

    def delete_income(self, name, user_id):
        cursor = self._connection.cursor()
        sql = 'delete from income where name=:name and user_id=:user_id'
        cursor.execute(sql, {'name':name, 'user_id':user_id})
        self._connection.commit()

    def delete_expense(self, name, user_id):
        cursor = self._connection.cursor()
        sql = 'delete from expenses where name=:name and user_id=:user_id'
        cursor.execute(sql, {'name':name, 'user_id':user_id})
        self._connection.commit()

    def add_wealth(self, wealth, user_id):
        cursor = self._connection.cursor()
        sql = 'insert into wealth (amount, user_id) values (:wealth, :user_id)'
        cursor.execute(sql, {'wealth':wealth, 'user_id':user_id})
        self._connection.commit()

    def register(self, username, password):
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
        cursor = self._connection.cursor()
        sql = 'select password from users where username=:username'
        result = cursor.execute(sql, {'username':username})
        try:
            right_password = result.fetchone()[0]
        except:
            return False
        return password == right_password

    def user_id(self, username):
        cursor = self._connection.cursor()
        sql = 'select id from users where username=:username'
        result = cursor.execute(sql, {'username':username})
        return result.fetchone()[0]

    def delete_user(self, username):
        cursor = self._connection.cursor()
        sql = 'delete from users where username=:username'
        cursor.execute(sql, {'username':username})
        self._connection.commit()