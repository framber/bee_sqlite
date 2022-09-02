import data_strings


def test_positive_one_insert(db_start_close):
    db = db_start_close
    db.execute("INSERT INTO client VALUES(?, ?, ?)", data_strings.P_DATA)
    db.commit()
    result = db.execute('SELECT * FROM client').fetchall()
    assert result[-1] == data_strings.P_DATA


def test_positive_multi_insert(db_start_close):
    db = db_start_close
    db.executemany("INSERT INTO client VALUES(?, ?, ?)", data_strings.P_MULTI_DATA)
    db.commit()
    result = db.execute('select * from client').fetchall()
    for item in data_strings.P_MULTI_DATA:
        assert item in result


def test_positive_one_update(db_start_close):
    db = db_start_close
    db.execute("""UPDATE client SET Name = "Holy Molly" where Name = "Mark"
    """)
    db.commit()
    result = db.execute('SELECT Name FROM client where Name = "Holy Molly"').fetchone()
    assert result[0] == "Holy Molly"


def test_positive_one_delete(db_start_close):
    db = db_start_close
    db.execute("""DELETE FROM client WHERE Id = 3
    """)
    db.commit()
    result = db.execute('SELECT * FROM client').fetchall()
    assert len(result) == 2

# Не пишу негативные тесты, так как пока не понимаю особо как работает assert
# с пустыми строками в БД
