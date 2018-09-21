import sqlite3

class Model:
    def __init__(self):
        self.__file_name = None
        self.__connection = None
        self.__cursor = None

    # connect to db
    def __connect(self):
        self.__connection = sqlite3.connect(self.__file_name)
        self.__cursor = self.__connection.cursor()

    # closes connection
    def __disconnect(self):
        pass
        self.__cursor.close()
        self.__connection.close()

    # creates a new mysql file(notebook)
    def create_noteBook(self,file_name):
        self.__file_name=file_name
        try:
            self.__connect()
            self.__cursor.execute("CREATE TABLE ITEMS (ID INTEGER PRIMARY KEY AUTOINCREMENT, ITEM VARCHAR(35), NOTE VARCHAR(10000))")
            self.__connection.commit()
        except sqlite3.OperationalError as er:
            #TODO error msg
            pass
        finally:
            self.__disconnect()

    # open a new mysql file(notebook)
    def open_noteBook(self,file_name):
        self.__file_name = file_name
        try:
            result = None
            self.__connect()
            self.__cursor.execute("SELECT * FROM ITEMS")
            self.__connection.commit()
            result = self.__cursor.fetchall()
        except sqlite3.OperationalError as er:
            #TODO error msg
            print(er)
        finally:
            self.__disconnect()
            return result

    # inserts a new index item
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

    # deletes index item
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

    # updates an index item
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

    # updates the index items if moved with ctrl+cursorKeys
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

    # loads the corresponding note
    def load_note(self,item):
        try:
            self.__connect()
            self.__cursor.execute(f"SELECT NOTE FROM ITEMS WHERE ITEM ='{item}'")
            self.__connection.commit()
            result = self.__cursor.fetchall()
        except sqlite3.OperationalError as er:
            # TODO mensaje de error
            print(er)
        finally:
            self.__disconnect()
            return result[0][0]

    # updates note text
    def update_note_text(self,text,item):
        try:
            self.__connect()
            self.__cursor.execute("UPDATE ITEMS SET NOTE=? WHERE ITEM=?",(text,item))
            self.__connection.commit()
        except sqlite3.OperationalError as er:
            # TODO mensaje de error
            print(er)
        finally:
            self.__disconnect()
