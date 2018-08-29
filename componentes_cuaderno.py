import sqlite3

class Cuaderno:
    def __init__(self,nombre_ruta):
        self.__nombre_ruta = str(nombre_ruta)
        self.__ruta = ""
        self.__nombre = ""
        self.__extension = ""
        self.__dividir_nombre_ruta_extension()

    def get_nombre(self):
        return self.__nombre

    def get_ruta(self):
        return self.__ruta

    def get_extension(self):
        return self.__extension

    def get_nombre_ruta(self):
        return self.__nombre_ruta

    # separa la ruta completa en elementos individuales ruta,nombre archivo y extension
    def __dividir_nombre_ruta_extension(self):
        # separa extension
        extension_tmp = self.__nombre_ruta.split(".")
        self.__extension = extension_tmp[-1]

        # separa nombre
        nombre_tmp =self.__nombre_ruta.split("/")
        ultimo_elemento = nombre_tmp[-1]
        nombre = ultimo_elemento.split(".")
        nombre_final = nombre[0]
        self.__nombre = nombre_final

        # separa ruta
        ruta_temp = self.__nombre_ruta.replace(ultimo_elemento)
        self.__ruta = ruta_temp

    #TODO
    def crear_cuaderno(self):
        pass
        '''mi_conexion = sqlite3.connect("primera_base")  # se conecta, si no existe la crea

        mi_cursor = mi_conexion.cursor()  # creamos cursor o puntero

        # crea la tabla si no existe , si se vuelve a ejeccutar esto genera error porque la tabla ya existe
        mi_cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

        # inserto datos
        # creo lista, si son varios una lista de tuplas.
        lista = ["BALON", 15, "DEPORTES"]
        mi_cursor.execute("INSERT INTO PRODUCTOS VALUES(?,?,?)", lista)

        # confirmo el cambio (siempre que se modifique la estructura de la tabla)
        mi_conexion.commit()

        mi_cursor.close()  # cierro el cursor
        mi_conexion.close()  # cierro la conexion'''



class Nota:
    pass

class item_indice:
    pass


