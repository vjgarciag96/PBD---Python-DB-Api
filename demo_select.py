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

def select_queries(cursor):
    selectpoblacionquery = "SELECT * FROM poblacion"
    selectsectoresquery = "SELECT * FROM sectores"

    cursor.execute(selectsectoresquery)
    data = cursor.fetchall()
    rowcount = cursor.rowcount
    print("------Numero de sectores: " + str(rowcount))
    print("-------- Sectores ----------")
    print_cursor_result_sectores(data)
    print('\n')

    cursor.execute(selectpoblacionquery)
    data = cursor.fetchall()
    rowcount = cursor.rowcount
    print("------Numero de personas: " + str(rowcount))
    print("-------- Población ----------")
    print_cursor_result_poblacion(data)
    print('\n')

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

if __name__ == '__main__':
    connection = stablish_connection()
    cursor = create_cursor(connection)

    select_queries(cursor)

    close_cursor(cursor)
    close_connection(connection)