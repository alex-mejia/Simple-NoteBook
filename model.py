import sqlite3

class Model:
    def __init__(self):
        self.__file_name = None
        self.__connection = None
        self.__cursor = None

    def __connect(self):
        self.__connection = sqlite3.connect(self.__file_name)
        self.__cursor = self.__connection.cursor()

    def __disconnect(self):
        self.__cursor.close()
        self.__connection.close()

    def create_noteBook(self,file_name):
        self.__file_name=file_name
        try:
            self.__connect()
            self.__cursor.execute("CREATE TABLE ITEMS (ID INTEGER PRIMARY KEY AUTOINCREMENT, ITEM VARCHAR(35))")
            self.__cursor.execute("CREATE TABLE NOTES (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOTE VARCHAR(10000))")
            self.__connection.commit()
        except sqlite3.OperationalError as er:
            #TODO mensaje de error
            pass
        finally:
            self.__disconnect()



