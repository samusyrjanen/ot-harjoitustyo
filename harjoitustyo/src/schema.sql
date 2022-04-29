CREATE TABLE expenses (
        id integer primary key,
        amount integer,
        name text,
        user_id integer references users
    );
CREATE TABLE income (
        id integer primary key,
        amount integer,
        name text,
        user_id integer references users
    );
CREATE TABLE wealth (
        id integer primary key,
        amount integer,
        user_id integer references users
    );
CREATE TABLE users (
        id integer primary key,
        username text unique,
        password text
    );
