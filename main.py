from tkinter import *

import constantes
from cuaderno import Cuaderno
from cuadernos_toolbar import *
raiz = Tk()


def centrar_ventana():
    screen_width = raiz.winfo_screenwidth()
    screen_height = raiz.winfo_screenheight()
    x_coordinate = (screen_width/2) - (constantes.WIDTH_OF_WINDOW/2)
    y_coordinate = (screen_height / 2) - (constantes.HEIGHT_OF_WINDOW / 2)
    return x_coordinate,y_coordinate

xpos = int(centrar_ventana()[0])
ypos = int(centrar_ventana()[1])

raiz.configure(background='black')
raiz.geometry(f"{constantes.WIDTH_OF_WINDOW}x{constantes.HEIGHT_OF_WINDOW}+{xpos}+{ypos}")
raiz.columnconfigure(0, weight=1)
raiz.rowconfigure(0, weight=1)
raiz.rowconfigure(1, weight=5)
############################################# DEFINCIO DE WIDGETS#######################################################

######################################## maneja el frame top donde iran los cuadernos
frame_top = Frame(raiz,bg='orange')
frame_top.grid(row=0, column=0, sticky=W  + N + S)
frame_top.rowconfigure(0,weight=1)

frame_top_agregar_cuaderno = Frame(frame_top,bg='#404040')
frame_top_agregar_cuaderno.grid(row=0,column=0,sticky=N+S+W)
frame_top_agregar_cuaderno.rowconfigure(0,weight=1)
btn_agregar_cuaderno = Label(frame_top_agregar_cuaderno,text="+",bg='#404040',
                             font=Font(family="Sans Serif", size=20),fg='yellow',cursor="hand2")
btn_agregar_cuaderno.bind("<Button-1>",lambda event:BarraCuadernos.crea_acceso_directo(frame_top))
btn_agregar_cuaderno.grid(row=0,column=0,padx=10,sticky=N+S)

######################################## contenedor para la nota y el indice
frame_botton = Frame(raiz)
frame_botton.grid(row=1, column=0, sticky=W + E + N + S)
frame_botton.rowconfigure(0, weight=1)
frame_botton.columnconfigure(0, weight=0)
frame_botton.columnconfigure(1, weight=2)

########################################## frame donde va el indice y las herramientas del indice
frame_left = Frame(frame_botton)
frame_left.grid(row=0, column=0, sticky=W + E + N + S)
frame_left.rowconfigure(0,weight=0)
frame_left.rowconfigure(1, weight=5)
frame_left.columnconfigure(0,weight=1)

########################################### frame donde van las herramientas de los items
frame_left_top = Frame(frame_left, bg="#9999ff")
frame_left_top.grid(row=0,column=0,sticky=N + S + W + E,padx=1,pady=1)

########################################### frame donde van los items del inidice
frame_left_botton = Frame(frame_left, bg='#b3b3ff')
frame_left_botton.grid(row=1, column=0, sticky= N + S + W + E,padx=1,pady=1)
frame_left_botton.columnconfigure(0,weight=1)
frame_left_botton.rowconfigure(0,weight=1)

########################################### frame donde va la nota
frame_right = Frame(frame_botton)
frame_right.grid(row=0, column=1, sticky=W + E + N + S)
frame_right.columnconfigure(0,weight=1)
frame_right.rowconfigure(0,weight=1)

########################################### controles de los indices
entry_item = Entry(frame_left_top,width=30,state='disabled')
entry_item.grid(row=0,column=0,padx=2,pady=10)

chk_es_seccion = Checkbutton(frame_left_top, text="Seccion", bg="#9999ff",state='disabled')
chk_es_seccion.grid(row=0, column=1, pady=10)

lst_items = Listbox(frame_left_botton, bg='#b3b3ff',borderwidth=0, highlightthickness=0,
                            font=Font(family="Sans Serif", size=11))
lst_items.grid(row=0,column=0,sticky= N + S + W + E ,padx=5,pady=5)

scroll_vertical = Scrollbar(frame_left_botton, command=lst_items.yview)
scroll_vertical.grid(row=0, column=1, sticky="nsew")
lst_items.config(yscrollcommand=scroll_vertical.set)

############################################ control de las notas
nota = Text(frame_right,bg='#ffff99',font=Font(family="Sans Serif", size=11),state='disabled')
nota.grid(row=0,column=0, sticky = N+S+E+W,padx=5,pady=5)

scroll_vertical = Scrollbar(frame_right, command=nota.yview)
scroll_vertical.grid(row=0, column=1, sticky="nsew")
nota.config(yscrollcommand=scroll_vertical.set)

############################################# menus
barra_menu = Menu(raiz)
archivo_menu = Menu(barra_menu,tearoff=False)
ayuda_menu = Menu(barra_menu,tearoff=False)


archivo_menu.add_command(label="Crear cuaderno",command=lambda :Cuaderno().crear_cuaderno(entry_item,chk_es_seccion))

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

raiz.config(menu=barra_menu)

#######################################################################################################################

raiz.mainloop()




















