from tkinter import Tk,ACTIVE
from view import *
from model import *
from tkinter import filedialog
from  notebook import *
from tkinter import messagebox

class Controller:
    def __init__(self):
        self.root = Tk()
        self.view = View(self.root)
        self.menu_bar = self.view.menu_bar
        self.model = Model()
        self.note_book = NoteBook()

        self.items_list = self.view.index_panel.items_list
        self.items_list.bind('<<ListboxSelect>>',self.get_selected_item)
        self.items_list.bind('<Control-Down>',self.move_item_down)
        self.items_list.bind('<Control-Up>', self.move_item_up)
        self.items_list.bind('<Delete>', self.delete_item)
        self.items_list.bind('<Double-Button-1>', self.get_edit_item)

        self.entry_item = self.view.index_panel.entry

        self.entry_item.bind('<FocusOut>', lambda event: print("foco perdido"))
        self.entry_item.bind('<Return>', self.insert_or_update_item)

        self.item_edit_mode = False
        self.current_item = None


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
        nb_file_path = filedialog.asksaveasfilename(defaultextension='.snb', title="New Simple NoteBook",
                                                        filetypes=(('Files spn', '*.ntb'),))
        self.note_book.set_nb_path(nb_file_path)

        if  nb_file_path == "":
            return
        else:
            self.model.create_noteBook(nb_file_path)
            self.view.index_panel.chk_is_section.config(state='normal')
            self.view.index_panel.entry.config(state='normal')
            self.view.index_panel.entry.focus_set()
            self.view.note_panel.note_text.config(state='normal')

    def entry_new_item(self, event):
        if self.entry_item.get() is not "":
            self.items_list.insert(END, self.entry_item.get())
            self.entry_item.delete(0, END)

    def get_selected_item(self,event):
        try:
            return self.items_list.curselection()[0]
        except IndexError:
            return None

    def move_item_down(self,event):
        current_item_index=self.get_selected_item(self)
        current_item_text = self.items_list.get(self.items_list.curselection())
        next_item_index=self.get_selected_item(self) + 1

        self.items_list.delete(current_item_index)
        self.items_list.insert(next_item_index,current_item_text)

    def move_item_up(self,event):
        current_item_index = self.get_selected_item(self)
        current_item_text = self.items_list.get(self.items_list.curselection())
        previous_item_index = self.get_selected_item(self) - 1

        self.items_list.delete(current_item_index)
        self.items_list.insert(previous_item_index, current_item_text)
        #selects the moved item
        self.items_list.activate(current_item_index)

    def delete_item(self,event):
        self.current_item = self.get_selected_item(event)
        if  self.current_item is not None:
            result = messagebox.askquestion("Delete","Delete item?")
            if result == "yes" and self.current_item is not None:
                self.items_list.delete(self.current_item)
                self.entry_item.delete(0, END)

    def insert_or_update_item(self,event):
        if self.item_edit_mode:
            self.items_list.delete(self.current_item)
            self.items_list.insert(self.current_item, self.entry_item.get())
            self.entry_item.delete(0, END)
            self.item_edit_mode = False
        else:
            self.entry_new_item(event)

    def get_edit_item(self,event):
        self.entry_item.delete(0, END)
        self.entry_item.insert(0,self.items_list.get(self.items_list.curselection()))

        self.current_item = self.get_selected_item(event)

        self.item_edit_mode = True


