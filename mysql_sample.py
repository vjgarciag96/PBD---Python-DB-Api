import MySQLdb

def stablish_connection():
    connection = MySQLdb.connect('localhost', 'pbd_user', '', 'pbd_sample')
    return connection

def close_cursor(cursor):
    cursor.close()

def close_connection(connection):
    connection.close()

def create_cursor(connection):
    return connection.cursor()

# Consultas de selección
def select_queries(cursor):
    selectpoblacionquery = "SELECT * FROM poblacion"
    selectsectoresquery = "SELECT * FROM sectores"
    cursor.execute(selectsectoresquery)
    #tambien podemos ir cogiendolos de uno en uno con fetchOne()
    data = cursor.fetchall()
    rowcount = cursor.rowcount
    print("------Numero de sectores: " + str(rowcount))
    print("-------- Sectores ---------- \n" + str(data))
    print_cursor_result_sectores(data)
    cursor.execute(selectpoblacionquery)
    data = cursor.fetchall()
    rowcount = cursor.rowcount
    print("------Numero de personas: " + str(rowcount))
    print('\n')
    print("-------- Población ---------- \n" + str(data))
    print_cursor_result_poblacion(data)

#Eliminación de las tablas
def drop_queries(cursor):
    dropsectoresquery = "DROP TABLE IF EXISTS sectores"
    droppoblacionquery = "DROP TABLE IF EXISTS poblacion"
    cursor.execute(droppoblacionquery)
    cursor.execute(dropsectoresquery)

#Creación de las tablas
def create_queries(cursor):
    createsectoresquery = """CREATE TABLE sectores (
                                  codS INT,
                                  nombreS VARCHAR(20),
                                  porcentS INT,
                                  ingresosS INT,
                                  PRIMARY KEY (codS)
                                )"""
    createpoblacionquery = """CREATE TABLE poblacion (
                                  dni VARCHAR(9),
                                  nombre VARCHAR(12),
                                  apellido1 VARCHAR(12),
                                  apellido2 VARCHAR(12),
                                  fechanac DATE,
                                  direccion VARCHAR(20),
                                  cp VARCHAR(5),
                                  sexo VARCHAR(1),
                                  ingresos INT,
                                  gastosFijos INT,
                                  gastosAlim INT,
                                  gastosRopa INT,
                                  sector INT,
                                  PRIMARY KEY (dni),
                                  FOREIGN KEY (sector) REFERENCES sectores (codS) ON DELETE SET NULL
                                );"""
    cursor.execute(createsectoresquery)
    cursor.execute(createpoblacionquery)

#Inserciones
def insert_queries(connection, cursor):
    try:
        cursor.execute("""INSERT INTO sectores
          VALUES (1,'Agricultura y pesca',0,0)""")
        cursor.execute("""INSERT INTO sectores
          VALUES (2,'Industria y energía',0,0)""")
        cursor.execute("""INSERT INTO sectores
          VALUES (3,'Servicios',0,0)""")
        cursor.execute("""INSERT INTO sectores
          VALUES (4,'Construcción',0,0)""")

        cursor.execute("""INSERT INTO poblacion
          VALUES ('123456789','Carlos','Gutiérrez','Pérez','19971115','Pz. Colón','06300','H',15000,4000,4000,3000,1)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('777888999','Gerardo','Martín','Duque','19611212','C. del Atún','06002','H',23000,6000,5000,4000,1)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('222333444','Pedro','Sánchez','González','19600201','C. Ancha','06300','H',22000,5000,3000,2000,1)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('333444555','María','García','Gil','19710410','C. Diagonal','06400','M',19500,3000,3000,3000,1)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('666884444','Ignacio','Costa','Burgos','19821212','C. Descubrimiento','10005','H',37000,5000,4500,2500,1)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('555666777','Vicente','Marañón','Fernández','19781115','Pz. América','10600','H',46000,8000,5000,4000,2)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('666777888','Beatriz','Losada','Gijón','19740412','Av. Principal','06400','M',50000,15000,8000,5000,2)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('888999000','Fernando','Huertas','Martínez','19710531','C. Mayor','06002','H',70000,20000,8000,4500,2)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('999000111','Francisco','Fernández','Merchán','19790312','C. Poniente','10800','H',63000,12000,7500,4500,2)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('666999333','Paula','Ordóñez','Ruiz','19900201','C. Atlántico','06800','M',25000,10000,3000,2000,2)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('987654321','Eva','Moreno','Pozo','19740510','C. Justicia','10005','M',40000,9000,6000,3000,3)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('111000111','Antonio','Muñoz','Hernández','19890701','C. Constitución','06800','H',25000,6500,3500,4000,3)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('111000222','Sara','Gálvez','Montes','19730407','C. Cádiz','10300','M',40000,11000,9500,6500,3)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('111000333','Cristina','Corral','Palma','19760512','C. Ermita','10600','M',48000,13000,7800,5200,3)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('111222333','Susana','Ruiz','Méndez','19990622','Av. Libertad','10800','M',18000,5000,4500,2500,3)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('444555666','Ángel','Montero','Salas','20000407','C. Tranquilidad','10300','H',14000,3000,3000,3000,4)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('888777666','Manuel','Vega','Zarzal','19761123','Pz. Azul','10005','H',36000,12000,6000,3000,4)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('333445555','Margarita','Guillén','Campos','19740319','Av. Héroes','06800','M',50000,12000,7500,6500,4)""")
        cursor.execute("""INSERT INTO poblacion
          VALUES ('222447777','Fermín','Hoz','Torres','19880808','C. Curva','06002','H',25000,4000,3000,2500,4)""")

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
    connection = stablish_connection()
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

    #TRANSACCIONES - A lo largo del codigo con commit() y rollback()
    #HANDLING ERRORS
    #1. Warning
    #2. Error
    #3. InterfaceError
    #4. DatabaseError
    #5. DataError
    #6. OperationError
    #7. IntegrityError
    #8. InternalError
    #9. ProgrammingError
    #10. NotSupportedError

    #URL - https://www.tutorialspoint.com/python/python_database_access.htm
    #URL - https://www.python.org/dev/peps/pep-0249/
    #Drivers
