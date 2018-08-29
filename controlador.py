from tkinter import filedialog

class Controlador:
    def __init__(self,raiz):
        self.__raiz = raiz

    def crear_cuaderno(self):
        archivo = filedialog.asksaveasfilename(defaultextension='.snb',initialdir="/", title="Crear nuevo Cuaderno",
                                               filetypes=(('Archivos spn','*.ntb'),))
        if archivo is None:
            return
        else:
            print(archivo)



