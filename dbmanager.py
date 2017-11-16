from db import DB

class dbmanager:
    db = None
    cursor = None

    def __init__(self, username = '', hostname = '', password = '', dbname = '', dbtype = '', profileName = None):
        if profileName == None:
            self.db = DB(username=username, hostname=hostname, password= password, dbname=dbname, dbtype=dbtype)
        else:
            self.db = DB()
            self.db = DB(profile=profileName)


    def save_profile(self, profileName):
        self.db.save_credentials()
        self.db.save_credentials(profile=profileName)

    def create_cursor(self):
        self.cursor = self.db.cur

    def close_cursor(self):
        self.cursor.close()

    def cursor_all_rows(self, query):
        count = self.cursor.execute(query)
        allRows = self.cursor.fetchall()
        print("Numero de tuplas: " + str(count))
        print(allRows)

    def cursor_one_row(self, query):
        count = self.cursor.execute(query)
        oneRow = self.cursor.fetchone()
        print("Numero de tuplas: 1")
        print(oneRow)

    def cursor_many_rows(self, query, rowsnumber):
        count = self.cursor.execute(query)
        manyRows = self.cursor.fetchmany(rowsnumber)
        print("Numero de tuplas: " + str(rowsnumber))
        print(manyRows)

    def dictionary_sample(self):
        cursor = self.db.cur
        dictionary = self.db.to_dict()#devuelve la definicion de las tablas en un diccionario
        print(dictionary)
        cursor.close

    def print_all_tables(self):
        print(self.db.tables)

    def execute_query(self, query):
        queryresult = self.db.query(query)
        print(queryresult)

    def execute_from_file(self, filename):
        print(self.db.query_from_file(filename))
        self.db.query_from_file(filename)
        print(self.db.query_from_file(filename))