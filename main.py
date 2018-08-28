#from tkinter import *
from gui import *

raiz = Tk()

def centrar_ventana():
    width_of_window = 1000
    height_of_window = 600

    screen_width = raiz.winfo_screenwidth()
    screen_height = raiz.winfo_screenheight()

    x_coordinate = (screen_width/2) - (width_of_window/2)
    y_coordinate = (screen_height / 2) - (height_of_window / 2)

    return x_coordinate,y_coordinate

xpos = int(centrar_ventana()[0])
ypos = int(centrar_ventana()[1])


raiz.configure(background='black')
raiz.geometry(f"1000x600+{xpos}+{ypos}")
raiz.columnconfigure(0, weight=1)
raiz.rowconfigure(0, weight=1)
raiz.rowconfigure(1, weight=9)

ui = Gui(raiz)

raiz.mainloop()

