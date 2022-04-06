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

    def clear(self):#not working for some reason
        cursor = self._connection.cursor()
        sql1 = 'delete from expenses'
        sql2 = 'delete from income'
        cursor.execute(sql1)
        cursor.execute(sql2)
        self._connection.commit()

'''class File_reader():
    def __init__(self):
        self.dirname = os.path.dirname(__file__)
        self.tulot_data_file_path = os.path.join(self.dirname, "repositoriot", "tulot.csv")
        self.menot_data_file_path = os.path.join(self.dirname, "repositoriot", "menot.csv")

    def read(self):
        earnings = []
        with open(self.tulot_data_file_path) as file:
            for row in file:
                row = row.replace('\n', '')
                parts = row.split(';')
                earnings.append(int(parts[0]))
            
        with open(self.menot_data_file_path) as file:
            for row in file:
                row = row.replace('\n', '')
                parts = row.split(';')
                earnings.append(int(parts[0]))

        return earnings

    def lisaa_tulo(self, sum: int, name):
        with open(self.tulot_data_file_path, 'a') as file:
            file.write(f'{sum};{name}\n')

    def lisaa_meno(self, sum: int, name):
        with open(self.menot_data_file_path, 'a') as file:
            file.write(f'{-sum};{name}\n')

    def clear(self):
        with open(self.tulot_data_file_path, 'w'):
            pass
        with open(self.menot_data_file_path, 'w'):
            pass'''