import os

class File_reader():
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

    def add(self, sum, name):
        with open(self.tulot_data_file_path, 'a') as file:
            file.write(f'{sum};{name}\n')

    def clear(self):
        with open(self.tulot_data_file_path, 'w'):
            pass