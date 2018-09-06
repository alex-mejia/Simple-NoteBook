# cuaderno de trabajo

from tkinter import filedialog
from modelo import *
import json

class Cuaderno:
    def __init__(self,raiz):
        self.__nombre_ruta = None
        self.__ruta = None
        self.__nombre = None
        self.__extension = None
        self.__raiz = raiz

    def crear_cuaderno(self,entry_local,chk_local):
        self.__nombre_ruta = filedialog.asksaveasfilename(defaultextension='.snb', initialdir="/",
                                                      title="Crear nuevo Cuaderno",
                                                      filetypes=(('Archivos spn', '*.ntb'),))
        if self.__nombre_ruta == "":
            return
        else:
            self.__dividir_nombre_ruta_extension()

            modelo = Modelo(self.__nombre_ruta)
            modelo.crear_cuaderno()

            entry_local.config(state = 'normal')
            chk_local.config(state = 'normal')

            self.__set_cuaderno_archivo_config()
            self.__raiz.title(self.__ruta+self.__nombre)

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
        ruta_temp = self.__nombre_ruta.replace(ultimo_elemento,"")
        self.__ruta = ruta_temp

    def __set_cuaderno_archivo_config(self):
        # lee diccionario desde json
        archivo = open("configuracion.json", "r")
        cadena = archivo.read()
        diccionario = json.loads(cadena)

        diccionario["cuadernos"].append({"ruta": self.__ruta, "nombre": self.__nombre, "extension": self.__extension})
        archivo.close()

        # escribe de regreso al json el nuevo cuaderno agregado
        cadena = json.dumps(diccionario)
        with open("configuracion.json", "w") as archivo:
            archivo.write(cadena)

