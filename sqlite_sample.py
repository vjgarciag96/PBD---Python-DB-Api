import sqlite3

def stablish_connection(database):
    conn = sqlite3.connect(database=database)
    return conn

def close_connection(connection):
    connection.close()

def create_cursor(conn):
    return conn.cursor()

def close_cursor(cursor):
    cursor.close()

def select_queries(cursor):
    selectpoblacionquery = "SELECT * FROM poblacion"
    selectsectoresquery = "SELECT * FROM sectores"
    cursor.execute(selectsectoresquery)
    #tambien podemos ir cogiendolos de uno en uno con fetchOne()
    data = cursor.fetchall()
    print("-------- Sectores ---------- \n" + str(data))
    print_cursor_result_sectores(data)
    cursor.execute(selectpoblacionquery)
    data = cursor.fetchall()
    print('\n')
    print("-------- Población ---------- \n" + str(data))
    print_cursor_result_poblacion(data)

def drop_queries(cursor):
    dropsectoresquery = "DROP TABLE IF EXISTS sectores"
    droppoblacionquery = "DROP TABLE IF EXISTS poblacion"
    cursor.execute(droppoblacionquery)
    cursor.execute(dropsectoresquery)

def create_queries(cursor):
    createsectoresquery = """CREATE TABLE sectores (
                                  codS INTEGER,
                                  nombreS TEXT,
                                  porcentS INTEGER,
                                  ingresosS INTEGER,
                                  PRIMARY KEY (codS)
                                )"""
    createpoblacionquery = """CREATE TABLE poblacion (
                                  dni TEXT,
                                  nombre TEXT,
                                  apellido1 TEXT,
                                  apellido2 TEXT,
                                  fechanac DATE,
                                  direccion TEXT,
                                  cp TEXT,
                                  sexo TEXT,
                                  ingresos INTEGER,
                                  gastosFijos INTEGER,
                                  gastosAlim INTEGER,
                                  gastosRopa INTEGER,
                                  sector INTEGER,
                                  PRIMARY KEY (dni),
                                  FOREIGN KEY (sector) REFERENCES sectores (codS) ON DELETE SET NULL
                                );"""
    cursor.execute(createsectoresquery)
    cursor.execute(createpoblacionquery)

def insert_queries(connection, cursor):
    try:
        with open('insert_script.sql', 'r') as myscript:
            data = myscript.read()
        cursor.executescript(data)
        connection.commit()
    except:
        print('Error inserting data')
        connection.rollback()


def update_queries(connection, cursor):
    updatesectoresquery = """UPDATE sectores SET nombreS = 'Desconocido' WHERE codS = 4"""
    updatepoblacionquery = """UPDATE poblacion SET cp = 20251 WHERE dni = '111000111'"""

    print("Contenido de las tuplas antes de la ejecución: ")
    cursor.execute("SELECT * FROM sectores WHERE codS = 4")
    sector = cursor.fetchone()
    print_sectores_row(sector)

    cursor.execute("SELECT * FROM poblacion WHERE dni = '111000111'")
    poblacion = cursor.fetchone()
    print_poblacion_row(poblacion)
    print('\n')

    try:
        cursor.execute(updatepoblacionquery)
        cursor.execute(updatesectoresquery)
        connection.commit()
    except:
        print("Error updating")
        connection.rollback()

    print("Contenido de las tuplas después de la ejecución: ")
    cursor.execute("SELECT * FROM sectores WHERE codS = 4")
    sector = cursor.fetchone()
    print_sectores_row(sector)

    cursor.execute("SELECT * FROM poblacion WHERE dni = '111000111'")
    poblacion = cursor.fetchone()
    print_poblacion_row(poblacion)

def delete_queries(connection, cursor):
    deletepoblacionquery = "DELETE FROM poblacion WHERE dni = '111000111'"
    try:
        cursor.execute(deletepoblacionquery)
        connection.commit()
        print("Deleted poblacion row with dni 111000111")
    except:
        connection.rollback()
        print("Error deleting row")

def print_sectores_row(row):
    print("--------------------------------------------")
    print("Sector " + str(row[0]) + ", " + str(row[1]))
    print("Ingresos = " + str(row[3]))
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
    connection = stablish_connection('pbd_sample')
    cursor = create_cursor(connection)

    print("Consultas de selección con la base de datos con varios registros")
    select_queries(cursor)
    print("Eliminación de todas las tablas")
    drop_queries(cursor)
    print("Creación de las tablas")
    create_queries(cursor)
    print("Consultas de selección con la base de datos vacia")
    select_queries(cursor)
    print("Inserciones en la base de datos")
    insert_queries(connection, cursor)
    print("Consultas de selección con las nuevas inserciones")
    select_queries(cursor)
    print("Consultas de actualización")
    update_queries(connection, cursor)
    print("Consultas de borrado")
    delete_queries(connection, cursor)

    close_cursor(cursor)
    close_connection(connection)
