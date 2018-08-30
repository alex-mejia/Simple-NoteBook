from tkinter import filedialog
from modelo import *

nombre_ruta = None
ruta = None
nombre = None
extension = None

def crear_cuaderno(entry_local,chk_local):
    global nombre_ruta
    nombre_ruta = filedialog.asksaveasfilename(defaultextension='.snb', initialdir="/",
                                                      title="Crear nuevo Cuaderno",
                                                      filetypes=(('Archivos spn', '*.ntb'),))
    if nombre_ruta is None:
        return
    else:
        dividir_nombre_ruta_extension()
        modelo = Modelo(nombre_ruta)
        modelo.crear_cuaderno()
        #entry_item.config(state = 'normal')
        entry_local.config(state = 'normal')
        chk_local.config(state = 'normal')

def dividir_nombre_ruta_extension():
        # separa extension
        extension_tmp = nombre_ruta.split(".")
        global extension
        extension = extension_tmp[-1]

        # separa nombre
        nombre_tmp =nombre_ruta.split("/")
        ultimo_elemento = nombre_tmp[-1]
        global nombre
        nombre = ultimo_elemento.split(".")
        nombre_final = nombre[0]
        nombre = nombre_final

        # separa ruta
        ruta_temp = nombre_ruta.replace(ultimo_elemento,"")
        global ruta
        ruta = ruta_temp