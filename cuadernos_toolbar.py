from tkinter import *
# maneja los accesos rapidos de los cuadernos creado en la barra de herramientas de la app

class BarraCuadernos:
    def agregar_cuaderno(self,padre,nombre_libro):

        ocultar_chars = len(nombre_libro)-16
        if len(nombre_libro) > 16:
            nombre_libro_tmp = nombre_libro[:-ocultar_chars] + '...'
        else:
            nombre_libro_tmp = nombre_libro
        btn_cuaderno = Button(padre,text=nombre_libro_tmp)
        btn_cuaderno.config(width=18,relief = GROOVE,bg='black',fg='white')
        btn_cuaderno.pack(side=LEFT,padx=20)

