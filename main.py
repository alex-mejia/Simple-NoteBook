#from tkinter import *
from gui import *

raiz = Tk()
raiz.configure(background='black')
raiz.geometry("1000x600")
raiz.columnconfigure(0, weight=1)
raiz.rowconfigure(0, weight=1)
raiz.rowconfigure(1, weight=10)

# TODO centrar la ventana

ui = Gui(raiz)

raiz.mainloop()