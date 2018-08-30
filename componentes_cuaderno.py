
from tkinter import filedialog
from modelo import *
from gui import Gui

class Cuaderno:
    def __init__(self):
        self.__nombre_ruta = None
        self.__ruta = None
        self.__nombre = None
        self.__extension = None


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
        ruta_temp = self.__nombre_ruta.replace(ultimo_elemento,"")
        self.__ruta = ruta_temp


    def crear_cuaderno(self):
        self.__nombre_ruta = filedialog.asksaveasfilename(defaultextension='.snb',initialdir="/", title="Crear nuevo Cuaderno",
                                               filetypes=(('Archivos spn','*.ntb'),))
        if self.__nombre_ruta is None:
            return
        else:
            self.__dividir_nombre_ruta_extension()
            modelo=Modelo(self.__nombre_ruta)
            modelo.crear_cuaderno()











class Nota:
    pass

class item_indice:
    pass


