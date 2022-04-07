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

    def read_wealth(self):
        cursor = self._connection.cursor()
        sql = 'select amount from wealth order by id desc'
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            return result[0]
        return 0

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
        sql3 = 'delete from wealth'
        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
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

    def add_wealth(self, wealth):
        cursor = self._connection.cursor()
        sql = 'insert into wealth (amount) values (:wealth)'
        cursor.execute(sql, {'wealth':wealth})
        self._connection.commit()
