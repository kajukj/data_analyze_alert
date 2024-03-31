import cx_Oracle as db


def database():
    oracle_connection = f'hr/admin@localhost:1521/xe'

    connection = db.connect(oracle_connection)

    cur = connection.cursor()

    return cur
