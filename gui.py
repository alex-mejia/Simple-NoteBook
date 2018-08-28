from tkinter import *
from tkinter.font import Font

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
        self._frame_botton.columnconfigure(0, weight=0)
        self._frame_botton.columnconfigure(1, weight=2)

        # frame donde va el indice y las herramientas del indice
        self._frame_left = Frame(self._frame_botton)
        self._frame_left.grid(row=0, column=0, sticky=W + E + N + S)
        self._frame_left.rowconfigure(0,weight=0)
        self._frame_left.rowconfigure(1, weight=5)
        self._frame_left.columnconfigure(0,weight=1)

        # frame donde van las herramientas de los items
        self._frame_left_top = Frame(self._frame_left, bg="#9999ff")
        self._frame_left_top.grid(row=0,column=0,sticky=N + S + W + E,padx=1,pady=1)

        # frame donde van los items del inidice
        self._frame_left_botton = Frame(self._frame_left, bg='#b3b3ff')
        self._frame_left_botton.grid(row=1, column=0, sticky= N + S + W + E,padx=1,pady=1)
        self._frame_left_botton.columnconfigure(0,weight=1)
        self._frame_left_botton.rowconfigure(0,weight=1)

        # frame donde va la nota
        self._frame_right = Frame(self._frame_botton)
        self._frame_right.grid(row=0, column=1, sticky=W + E + N + S)
        self._frame_right.columnconfigure(0,weight=1)
        self._frame_right.rowconfigure(0,weight=1)

        self.area_control_items()
        self.area_indices()
        self.area_nota()

    def area_control_items(self):
       entry_item = Entry(self._frame_left_top,width=30)
       entry_item.grid(row=0,column=0,padx=2,pady=10)

       chk_es_seccion = Checkbutton(self._frame_left_top, text="Seccion", bg="#9999ff")
       chk_es_seccion.grid(row=0, column=1, pady=10)

    def area_indices(self):
        lst_items = Listbox(self._frame_left_botton, bg='#b3b3ff',borderwidth=0, highlightthickness=0,
                            font=Font(family="Sans Serif", size=11))
        lst_items.grid(row=0,column=0,sticky= N + S + W + E ,padx=5,pady=5)

        #for i in range(30):
            #lst_items.insert(END,i)

        scroll_vertical = Scrollbar(self._frame_left_botton, command=lst_items.yview)
        scroll_vertical.grid(row=0, column=1, sticky="nsew")
        lst_items.config(yscrollcommand=scroll_vertical.set)

    def area_nota(self):
        nota = Text(self._frame_right,bg='#ffff99',font=Font(family="Sans Serif", size=11))
        nota.grid(row=0,column=0, sticky = N+S+E+W,padx=5,pady=5)

        scroll_vertical = Scrollbar(self._frame_right, command=nota.yview)
        scroll_vertical.grid(row=0, column=1, sticky="nsew")
        nota.config(yscrollcommand=scroll_vertical.set)










