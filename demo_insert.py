import MySQLdb

def stablish_connection():
    connection = MySQLdb.connect('localhost', 'pbd_user', '', 'pbd_sample')
    return connection

def close_connection(connection):
    connection.close()

def create_cursor(connection):
    return connection.cursor()

def close_cursor(cursor):
    cursor.close()

def insert_queries(connection, cursor):
    try:
        cursor.executescript('insert_script.sql')
        connection.commit()
    except:
        print('Error inserting data')
        connection.rollback()

if __name__ == '__main__':
    connection = stablish_connection()
    cursor = create_cursor(connection)

    insert_queries(connection, cursor)

    close_cursor(cursor)
    close_connection(connection)
