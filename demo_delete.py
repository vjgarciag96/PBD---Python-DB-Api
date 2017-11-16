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

def print_sectores_row(row):
    print("--------------------------------------------")
    print("Sector " + str(row[0]) + ", " + str(row[1]))
    print("Ingresos -> " + str(row[3]))
    print("Porcentaje respecto al total -> " + str(row[2]))

def print_poblacion_row(row):
    print("--------------------------------------------")
    print("DNI " + str(row[0]) + " - " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))
    print("Fecha de nacimiento: " + str(row[4]))
    print("Dirección: " + str(row[5]))
    print("Codigo postal: " + str(row[6]))
    print("Sexo: " + str(row[7]))
    print("Ingresos: " + str(row[8]))
    print("Gastos fijos: " + str(row[9]))
    print("Gastos alimentación: " + str(row[10]))
    print("Gastos ropa: " + str(row[11]))
    print("Sector: " + str(row[12]))

def print_cursor_result_sectores(result):
    try:
        for row in result:
            print_sectores_row(row)
    except:
        print("Error: Unable to fetch data")
    print("--------------------------------------------")


def print_cursor_result_poblacion(result):
    try:
        for row in result:
            print_poblacion_row(row)
    except:
        print("Error: Unable to fetch data")
    print("--------------------------------------------")

def delete_queries(connection, cursor):
    deletepoblacionquery = "DELETE FROM poblacion WHERE dni = '111000111'"
    try:
        cursor.execute(deletepoblacionquery)
        connection.commit()
        print("Deleted poblacion row with dni 111000111")
    except:
        connection.rollback()
        print("Error deleting row")

if __name__ == '__main__':
    connection = stablish_connection()
    cursor = create_cursor(connection)

    delete_queries(connection, cursor)

    close_cursor(cursor)
    close_connection(connection)