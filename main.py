from gui import *

raiz = Tk()

width_of_window = 1150
height_of_window = 600

def centrar_ventana():


    screen_width = raiz.winfo_screenwidth()
    screen_height = raiz.winfo_screenheight()

    x_coordinate = (screen_width/2) - (width_of_window/2)
    y_coordinate = (screen_height / 2) - (height_of_window / 2)

    return x_coordinate,y_coordinate

xpos = int(centrar_ventana()[0])
ypos = int(centrar_ventana()[1])


raiz.configure(background='black')
raiz.geometry(f"{width_of_window}x{height_of_window}+{xpos}+{ypos}")
raiz.columnconfigure(0, weight=1)
raiz.rowconfigure(0, weight=1)
raiz.rowconfigure(1, weight=2)

ui = Gui(raiz)

raiz.mainloop()

