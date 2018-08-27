from tkinter import *

class Gui:
    def __init__(self,raiz):
        self._raiz = raiz

        # maneja el frame top donde iran los cuadernos
        self._frame_top = Frame(self._raiz,bg='red')
        self._frame_top.grid(row=0, column=0, sticky=W + E + N + S)

        # contenedor para la nota y el indice
        self._frame_botton = Frame(raiz, bg='blue')
        self._frame_botton.grid(row=1, column=0, sticky=W + E + N + S)
        self._frame_botton.rowconfigure(0, weight=1)
        self._frame_botton.columnconfigure(0, weight=1)
        self._frame_botton.columnconfigure(1, weight=3)

        # frame donde va el indice y las herramientas del indice
        self._frame_left = Frame(self._frame_botton, bg='yellow')
        self._frame_left.grid(row=0, column=0, sticky=W + E + N + S)

        # frame donde va la nota
        self._frame_right = Frame(self._frame_botton, bg='green')
        self._frame_right.grid(row=0, column=1, sticky=W + E + N + S)

       # TODO agregar frame de las herramientas del indice

    def area_control_items(self):
       pass