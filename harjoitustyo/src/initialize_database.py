from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists expenses;
    ''')
    cursor.execute('''
        drop table if exists income;
    ''')
    cursor.execute('''
        drop table if exists wealth;
    ''')
    cursor.execute('''
        drop table if exists users;
    ''')

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE expenses (
            id integer primary key,
            amount integer,
            name text,
            user_id integer references users
        );
    ''')
    cursor.execute('''
        CREATE TABLE income (
            id integer primary key,
            amount integer,
            name text,
            user_id integer references users
        );
    ''')
    cursor.execute('''
        CREATE TABLE wealth (
            id integer primary key,
            amount integer,
            user_id integer references users
        );
    ''')
    cursor.execute('''
        CREATE TABLE users (
            id integer primary key,
            username text unique,
            password text
        );
    ''')

    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
