from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists expenses;
    ''')
    cursor.execute('''
        drop table if exists income;
    ''')

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table expenses (
            id integer primary key,
            amount integer,
            name text
        );
    ''')
    cursor.execute('''
        create table income (
            id integer primary key,
            amount integer,
            name text
        );
    ''')

    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
