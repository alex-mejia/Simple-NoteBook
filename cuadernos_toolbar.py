from tkinter import Label
from tkinter.font import Font

# maneja los accesos rapidos de los cuadernos creado en la barra de herramientas de la app

class BarraCuadernos:
  ruta_cuaderno = None
  nombre_cuaderno = None
  extension_cuaderno = None

  @staticmethod
  def crea_acceso_directo(padre):
      numero_actual = len(padre.children.values())
      acceso_directo = Label(padre,text=BarraCuadernos.nombre_cuaderno,bg="black",fg="yellow",font=Font(family="Sans Serif", size=12))

      acceso_directo.grid(row=0,column=numero_actual,padx=10)





