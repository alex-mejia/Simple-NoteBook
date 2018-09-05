from tkinter import Label
from tkinter.font import Font
from tkinter import messagebox
import constantes

# maneja los accesos rapidos de los cuadernos creado en la barra de herramientas de la app

class BarraCuadernos:
  ruta_cuaderno = None
  nombre_cuaderno = None
  extension_cuaderno = None

  @staticmethod
  def crea_acceso_directo(padre):
      numero_actual = len(padre.children.values())

      nombre_cuaderno = BarraCuadernos.nombre_cuaderno

      limite_derecho_padre = padre.winfo_width() #el tamaño del frame top

      if limite_derecho_padre >= constantes.WIDTH_OF_WINDOW-250:
          messagebox.showwarning("No se pudo agregar Acceso directo", "Favor elimine algun acceso directo para agregar mas.")
      elif nombre_cuaderno is None:
          messagebox.showwarning("No se pudo agregar Acceso directo", "Favor abra o cree un cuaderno.")
      else:
          acceso_directo = Label(padre, text=BarraCuadernos.nombre_cuaderno, bg="black", fg="yellow",
          font=Font(family="Sans Serif", size=12))
          acceso_directo.grid(row=0,column=numero_actual,padx=10)

      BarraCuadernos.nombre_cuaderno = None







