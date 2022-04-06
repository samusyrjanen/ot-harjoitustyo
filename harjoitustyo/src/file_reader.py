class Repository:
    def __init__(self, connection):
        self._connection = connection

    def read_expenses(self):
        cursor = self._connection.cursor()
        sql = 'select amount from expenses'
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [row['amount'] for row in rows]

    def read_income(self):
        cursor = self._connection.cursor()
        sql = 'select amount from income'
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [row['amount'] for row in rows]

    def add_expense(self, amount, name):
        cursor = self._connection.cursor()
        sql = 'insert into expenses (amount, name) values ' \
            '(:amount, :name)'
        cursor.execute(sql, {'amount':amount, 'name':name})
        self._connection.commit()

    def add_income(self, amount, name):
        cursor = self._connection.cursor()
        sql = 'insert into income (amount, name) values ' \
            '(:amount, :name)'
        cursor.execute(sql, {'amount':amount, 'name':name})
        self._connection.commit()

    def clear(self):
        cursor = self._connection.cursor()
        sql1 = 'delete from expenses'
        sql2 = 'delete from income'
        cursor.execute(sql1)
        cursor.execute(sql2)
        self._connection.commit()

    def get_data_expenses(self):
        cursor = self._connection.cursor()
        sql = 'select amount, name from expenses'
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [(row['amount'], row['name']) for row in rows]

    def get_data_income(self):
        cursor = self._connection.cursor()
        sql = 'select amount, name from income'
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [(row['amount'], row['name']) for row in rows]

    def delete_income(self, name):
        cursor = self._connection.cursor()
        sql = 'delete from income where name=:name'
        cursor.execute(sql, {'name':name})
        self._connection.commit()

    def delete_expense(self, name):
        cursor = self._connection.cursor()
        sql = 'delete from expenses where name=:name'
        cursor.execute(sql, {'name':name})
        self._connection.commit()
