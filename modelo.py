# operaciones en las bases de datos

import sqlite3

class Modelo:
    def __init__(self,nombre_bdd):
        self.__nombre_bdd = nombre_bdd
        self.__conexion = None
        self.__cursor = None

    def __conectar_bdd(self):
        self.__conexion = sqlite3.connect(self.__nombre_bdd)
        self.__cursor = self.__conexion.cursor()

    def __desconectar_bdd(self):
        self.__cursor.close()
        self.__conexion.close()

    def crear_cuaderno(self):
        try:
            self.__conectar_bdd()
            self.__cursor.execute("CREATE TABLE ITEMS (ID INTEGER PRIMARY KEY AUTOINCREMENT, ITEM VARCHAR(35))")
            self.__cursor.execute("CREATE TABLE NOTAS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOTA VARCHAR(10000))")
            self.__conexion.commit()
        except sqlite3.OperationalError as er:
            #TODO mensaje de error
            pass
        finally:
            self.__desconectar_bdd()



