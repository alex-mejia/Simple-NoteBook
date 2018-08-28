from gui import *
import constantes

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
raiz.rowconfigure(1, weight=2)

ui = Gui(raiz)

raiz.mainloop()

