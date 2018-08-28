from tkinter import *

class Gui:
    def __init__(self,raiz):
        self._raiz = raiz

        # maneja el frame top donde iran los cuadernos
        self._frame_top = Frame(self._raiz,bg='black')
        self._frame_top.grid(row=0, column=0, sticky=W + E + N + S)

        # contenedor para la nota y el indice
        self._frame_botton = Frame(raiz)
        self._frame_botton.grid(row=1, column=0, sticky=W + E + N + S)
        self._frame_botton.rowconfigure(0, weight=1)
        self._frame_botton.columnconfigure(0, weight=1)
        self._frame_botton.columnconfigure(1, weight=3)

        # frame donde va el indice y las herramientas del indice
        self._frame_left = Frame(self._frame_botton)
        self._frame_left.grid(row=0, column=0, sticky=W + E + N + S)
        self._frame_left.rowconfigure(0,weight=1)
        self._frame_left.rowconfigure(1, weight=5)
        self._frame_left.columnconfigure(0,weight=1)

        # frame donde van las herramientas de los items
        self._frame_left_top = Frame(self._frame_left, bg="#9999ff")
        self._frame_left_top.grid(row=0,column=0,sticky=N + S + W + E)

        # frame donde van los items del inidice
        self._frame_left_botton = Frame(self._frame_left, bg='#b3b3ff')
        self._frame_left_botton.grid(row=1, column=0, sticky= N + S + W + E)

        # frame donde va la nota
        self._frame_right = Frame(self._frame_botton, bg='#ffff99')
        self._frame_right.grid(row=0, column=1, sticky=W + E + N + S)

    def area_control_items(self):
       pass