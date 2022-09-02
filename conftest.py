import sqlite3

import pytest


@pytest.fixture()
def db_start_close():
    db = sqlite3.connect(':memory:')
    print("Подключение к БД установлено. БД находится в оперативной памяти")
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS client(
            Id INTEGER PRIMARY KEY NOT NULL,
            Name TEXT NOT NULL,
            Change_Date TEXT NOT NULL)
            """)
    db.commit()

    first_data = [
        ("1", "Mark", "11.08.2022"),
        ("2", "Karl", "12.08.2022"),
        ("3", "Max", "13.08.2022"),
    ]
    sql.executemany("""INSERT INTO client(Id, Name, Change_Date) VALUES(?, ?, ?)""", first_data)
    db.commit()

    yield db

    db.close()
