import sqlite3 as sq

DATABASE = 'database.db'
SCHEME = 'schema.sql'


def connect_db():
    return sq.connect(DATABASE)


def create_db():
    connection = connect_db()
    cursor = connection.cursor()
    with open(SCHEME, mode='r') as file:
        scheme_script = file.read()
    cursor.executescript(scheme_script)
    connection.commit()
    cursor.close()
    connection.close()


def dict_factory(cursor, row):
    data = {}
    for idx, col in enumerate(cursor.description):
        data[col[0]] = row[idx]
    return data


def select_prizes(prize_id=None):
    this_list = []
    connection = connect_db()

    if prize_id is None:
        sql = "SELECT * FROM prize"
    else:
        sql = f"SELECT * FROM prize WHERE id = {prize_id}"

    try:
        cursor = connection.execute(sql)
        cursor.row_factory = dict_factory
        for row in cursor:
            record = {
                'id': row.get('id'),
                'description': row.get('description'),
            }
            this_list.append(record)

    except connection.Error as error:
        print("Error connection to database", error)
    finally:
        if connection: connection.close()

    return this_list


def select_participants(participant_id=None):
    this_list = []
    connection = connect_db()

    if participant_id is None:
        sql = "SELECT * FROM participant"
    else:
        sql = f"SELECT * FROM participant WHERE id = {participant_id}"

    try:
        cursor = connection.execute(sql)
        cursor.row_factory = dict_factory
        for row in cursor:
            record = {
                'id': row.get('id'),
                'name': row.get('name'),
            }
            this_list.append(record)

    except connection.Error as error:
        print("Error connection to database", error)
    finally:
        if connection: connection.close()
    return this_list


def select_promos(promo_id=None):
    this_list = []
    connection = connect_db()

    if promo_id is None:
        sql = "SELECT * FROM promo"
    else:
        sql = f"SELECT * FROM promo WHERE id = {promo_id}"

    try:
        cursor = connection.execute(sql)
        cursor.row_factory = dict_factory
        if promo_id is not None:
            for row in cursor:
                record = {
                    'id': row.get('id'),
                    'name': row.get('name'),
                    'description': row.get('description'),
                    'prizes': select_prizes(),
                    'participants': select_participants(),
                }
                this_list.append(record)
        else:
            for row in cursor:
                record = {
                    'id': row.get('id'),
                    'name': row.get('name'),
                    'description': row.get('description'),
                }
                this_list.append(record)

    except connection.Error as error:
        print("Error connection to database", error)
    finally:
        if connection: connection.close()

    return this_list


def insert_promo(name_input, description_input):
    connection = connect_db()
    this_list = []
    temp = 0
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO promo (name, description) VALUES (?, ?);"
        data_tuple = (name_input, description_input)
        count = cursor.execute(sql, data_tuple)
        temp = cursor.rowcount
        connection.commit()
        cursor.close()
    except connection.Error as error:
        print("Error connection to database", error)
    finally:
        if connection: connection.close()
    return temp