from tkinter import filedialog
from modelo import *

class Cuaderno:
    def __init__(self):
        self.__nombre_ruta = None
        self.__ruta = None
        self.__nombre = None
        self.__extension = None

    def crear_cuaderno(self,entry_local,chk_local):
        self.__nombre_ruta = filedialog.asksaveasfilename(defaultextension='.snb', initialdir="/",
                                                      title="Crear nuevo Cuaderno",
                                                      filetypes=(('Archivos spn', '*.ntb'),))
        if self.__nombre_ruta is None:
            return
        else:
            self.__dividir_nombre_ruta_extension()
            modelo = Modelo(self.__nombre_ruta)
            modelo.crear_cuaderno()
            entry_local.config(state = 'normal')
            chk_local.config(state = 'normal')

    def get_ruta_nombre_extension(self):
        return self.__ruta, self.__nombre, self.__extension

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

