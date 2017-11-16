from db import DB

class SQLiteDB:

    def __init__(self,schema):
        self.db=DB(dbtype="sqlite",filename=schema)
        self.cursor=self.db.cur

    def closeCursor(self):
        self.cursor.close()

    def getAllSectores(self):
        self.cursor.execute("SELECT * FROM SECTORES")
        return self.fetchall()

    def getSector(self,id):
        self.cursor.execute("SELECT * FROM SECTORES WHERE codS=?",id)
        return self.fetchone()

    def insertSector(self,codS,nombreS,porcentS,ingresosS):
        self.cursor.execute("INSERT INTO VALUES (?,?,?,?)",codS,nombreS,porcentS,ingresosS)
        return codS

    def deleteSector(self,id):
        self.cursor.execute("DELETE FROM SECTORES WHERE codS=?",id)

    def updateSector(self,nombreS,porcentS,ingresosS):
        self.cursor.execute("UPDATE SECOTRES SET nombreS, porcentS,ingresosS VALUES (?,?,?)",nombreS,porcentS,ingresosS)