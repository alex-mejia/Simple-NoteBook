from tkinter import Tk
from view import *
from model import *
from tkinter import filedialog

class Controller:
    def __init__(self):
        self.root = Tk()
        self.view = View(self.root)
        self.menu_bar = self.view.get_menu()
        self.model = Model()
        self.file_name = None

    def run(self):
        self.root.title("Simple NoteBook")

        self.root.columnconfigure(1, weight=4)
        self.root.rowconfigure(0,weight=1)
        self.root.deiconify()

        self.center_window()
        self.create_menu()
        self.root.mainloop()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (1100 / 2))
        y_coordinate = int((screen_height / 2) - (600 / 2))
        self.root.geometry(f"1100x600+{x_coordinate}+{y_coordinate}")

    def create_menu(self):
        menu_file = Menu(self.menu_bar, tearoff=False)
        menu_help = Menu(self.menu_bar, tearoff=False)

        menu_file.add_command(label="New NoteBook",command=lambda :self.create_noteBook())
        menu_file.add_command(label="Open NoteBook")
        menu_file.add_command(label="Close NoteBook")
        menu_file.add_separator()
        menu_file.add_command(label="Save Note")
        menu_file.add_command(label="Delete Note")
        menu_file.add_separator()
        menu_file.add_command(label="Exit")

        menu_help.add_command(label="Basic Guide")
        menu_help.add_command(label="Keyboard Shortcuts")

        self.menu_bar.add_cascade(label="File", menu=menu_file)
        self.menu_bar.add_cascade(label="Help", menu=menu_help)

        self.root.config(menu=self.menu_bar)

    def create_noteBook(self):
        self.file_name = filedialog.asksaveasfilename(defaultextension='.snb', title="New Simple NoteBook",
                                                         filetypes=(('Files spn', '*.ntb'),))
        if  self.file_name == "":
            return
        else:
            #self.__dividir_nombre_ruta_extension()
            self.model.create_noteBook(self.file_name)
            #entry_local.config(state='normal')
            #chk_local.config(state='normal')

