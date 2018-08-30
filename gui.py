from tkinter import *
from tkinter.font import Font
from componentes_cuaderno import *

class Gui:
    def __init__(self,raiz):
        self.__cuaderno = Cuaderno()

        self.__raiz = raiz

        # maneja el frame top donde iran los cuadernos
        self.__frame_top = Frame(self.__raiz,bg='black')
        self.__frame_top.grid(row=0, column=0, sticky=W + E + N + S)

        # contenedor para la nota y el indice
        self.__frame_botton = Frame(raiz)
        self.__frame_botton.grid(row=1, column=0, sticky=W + E + N + S)
        self.__frame_botton.rowconfigure(0, weight=1)
        self.__frame_botton.columnconfigure(0, weight=0)
        self.__frame_botton.columnconfigure(1, weight=2)

        # frame donde va el indice y las herramientas del indice
        self.__frame_left = Frame(self.__frame_botton)
        self.__frame_left.grid(row=0, column=0, sticky=W + E + N + S)
        self.__frame_left.rowconfigure(0,weight=0)
        self.__frame_left.rowconfigure(1, weight=5)
        self.__frame_left.columnconfigure(0,weight=1)

        # frame donde van las herramientas de los items
        self.__frame_left_top = Frame(self.__frame_left, bg="#9999ff")
        self.__frame_left_top.grid(row=0,column=0,sticky=N + S + W + E,padx=1,pady=1)

        # frame donde van los items del inidice
        self.__frame_left_botton = Frame(self.__frame_left, bg='#b3b3ff')
        self.__frame_left_botton.grid(row=1, column=0, sticky= N + S + W + E,padx=1,pady=1)
        self.__frame_left_botton.columnconfigure(0,weight=1)
        self.__frame_left_botton.rowconfigure(0,weight=1)

        # frame donde va la nota
        self.__frame_right = Frame(self.__frame_botton)
        self.__frame_right.grid(row=0, column=1, sticky=W + E + N + S)
        self.__frame_right.columnconfigure(0,weight=1)
        self.__frame_right.rowconfigure(0,weight=1)

        # controles de los indices
        self.entry_item = Entry(self.__frame_left_top,width=30,state='disabled')
        self.entry_item.grid(row=0,column=0,padx=2,pady=10)

        chk_es_seccion = Checkbutton(self.__frame_left_top, text="Seccion", bg="#9999ff",state='disabled')
        chk_es_seccion.grid(row=0, column=1, pady=10)

        lst_items = Listbox(self.__frame_left_botton, bg='#b3b3ff',borderwidth=0, highlightthickness=0,
                            font=Font(family="Sans Serif", size=11))
        lst_items.grid(row=0,column=0,sticky= N + S + W + E ,padx=5,pady=5)

        scroll_vertical = Scrollbar(self.__frame_left_botton, command=lst_items.yview)
        scroll_vertical.grid(row=0, column=1, sticky="nsew")
        lst_items.config(yscrollcommand=scroll_vertical.set)

        # control de las notas
        nota = Text(self.__frame_right,bg='#ffff99',font=Font(family="Sans Serif", size=11),state='disabled')
        nota.grid(row=0,column=0, sticky = N+S+E+W,padx=5,pady=5)

        scroll_vertical = Scrollbar(self.__frame_right, command=nota.yview)
        scroll_vertical.grid(row=0, column=1, sticky="nsew")
        nota.config(yscrollcommand=scroll_vertical.set)


        # menus
        barra_menu = Menu(self.__raiz)
        archivo_menu = Menu(barra_menu,tearoff=False)
        ayuda_menu = Menu(barra_menu,tearoff=False)

        archivo_menu.add_command(label="Crear cuaderno",command=self.__cuaderno.crear_cuaderno)
        archivo_menu.add_command(label="Cerrar cuaderno")
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Guardar nota")
        archivo_menu.add_command(label="Eliminar nota")
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir")

        ayuda_menu.add_command(label="Guia basica")
        ayuda_menu.add_command(label = "Atajos del teclado")

        barra_menu.add_cascade(label="Archivo",menu=archivo_menu)
        barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

        self.__raiz.config(menu=barra_menu)
















