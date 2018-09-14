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
            self.__cursor.execute("CREATE TABLE ITEMS (ID INTEGER PRIMARY KEY AUTOINCREMENT, ITEM VARCHAR(35), NOTE VARCHAR(10000))")
            self.__connection.commit()
        except sqlite3.OperationalError as er:
            #TODO mensaje de error
            pass
        finally:
            self.__disconnect()

    def insert_item(self,item,note):
        items = (item,note)
        try:
            self.__connect()
            self.__cursor.execute("INSERT INTO ITEMS VALUES(NULL,?,?)",(items))
            self.__connection.commit()
        except sqlite3.OperationalError as er:
            #TODO mensaje de error
            pass
        finally:
            self.__disconnect()

    def delete_item(self,item):
        try:
            self.__connect()
            self.__cursor.execute("DELETE FROM ITEMS WHERE ITEM = ?",(item,))
            self.__connection.commit()
        except sqlite3.OperationalError as er:
            #TODO mensaje de error
            pass
        finally:
            self.__disconnect()

    def update_item(self,new_item,old_item):
        try:
            self.__connect()
            self.__cursor.execute("UPDATE ITEMS SET ITEM=? WHERE ITEM=?",(new_item,old_item))
            self.__connection.commit()
        except sqlite3.OperationalError as er:
            #TODO mensaje de error
            pass
        finally:
            self.__disconnect()

    def update_item_postion(self,item_list):
        contador = 1
        try:
            self.__connect()

            for i in item_list:
                self.__cursor.execute("UPDATE ITEMS SET ITEM=? WHERE ID=?",(i,contador))
                contador = contador + 1

            self.__connection.commit()
        except sqlite3.OperationalError as er:
            #TODO mensaje de error
            print(er)
        finally:
            self.__disconnect()