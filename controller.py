from tkinter import Tk
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

        # update changes in db when exiting app
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # events for index items
        self.items_list = self.view.index_panel.items_list
        self.items_list.bind('<<ListboxSelect>>',self.get_selected_item)
        self.items_list.bind('<Control-Down>',self.move_item_down)
        self.items_list.bind('<Control-Up>', self.move_item_up)
        self.items_list.bind('<Delete>', self.delete_item)
        self.items_list.bind('<Double-Button-1>', self.get_edit_item)
        self.items_list.bind('<FocusOut>', self.update_item_position_db)

        # events for Entry box
        self.entry_item = self.view.index_panel.entry
        self.entry_item.bind('<Return>', self.insert_or_update_item)

        # events for note
        self.note = self.view.note_panel.note_text
        self.note.bind('<Control-s>',self.update_note)
        self.note.bind('<KeyPress>',self.note_text_changed)

        # globals
        self.item_edit_mode = False
        self.current_item = None
        self.current_item_text = None
        self.items_list_moved = None

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

    def on_closing(self):
        self.update_item_position_db()
        self.root.destroy()

    def create_menu(self):
        menu_file = Menu(self.menu_bar, tearoff=False)
        menu_help = Menu(self.menu_bar, tearoff=False)

        menu_file.add_command(label="New NoteBook",command=self.create_noteBook)
        menu_file.add_command(label="Open NoteBook",command=self.open_noteBook)
        menu_file.add_separator()
        menu_file.add_command(label="Save Note",command=self.update_note)
        menu_file.add_separator()
        menu_file.add_command(label="Exit",command= lambda :self.root.destroy())

        menu_help.add_command(label="Basic Guide")
        menu_help.add_command(label="Keyboard Shortcuts")

        self.menu_bar.add_cascade(label="File", menu=menu_file)
        self.menu_bar.add_cascade(label="Help", menu=menu_help)

        self.root.config(menu=self.menu_bar)

    def create_noteBook(self):
        nb_file_path = filedialog.asksaveasfilename(defaultextension='.snb', title="New Simple NoteBook",
                                                        filetypes=(('Files spn', '*.ntb'),))

        self.note_book.set_nb_path(nb_file_path)

        # if cancel
        if  nb_file_path == "":
            return
        else:
            self.entry_item.delete(0, END)
            self.items_list.delete(0,END)

            self.model.create_noteBook(nb_file_path)
            self.view.index_panel.entry.config(state='normal')
            self.view.index_panel.entry.focus_set()

            # sets the current created file to main window title
            self.root.title(nb_file_path)

    def open_noteBook(self):
        nb_file_path = filedialog.askopenfile(title="Open NoteBook", filetypes=(("Simple NoteBook files", "*.ntb"),))

        if nb_file_path is None:
            return
        else:
            self.note_book.set_nb_path(nb_file_path.name)
            index_list=self.model.open_noteBook(nb_file_path.name)

            self.view.index_panel.entry.config(state='normal')
            self.root.title(nb_file_path.name)

            # clear the listbox
            self.items_list.delete(0,END)
            # clear the entry
            self.view.index_panel.entry.delete(0,END)
            # clear the note
            self.note.delete(1.0,END)

            for i in index_list:
                self.items_list.insert(END,i[1])

    # for adding new index items
    def entry_new_item(self, event):
        if self.entry_item.get() is not "":
            self.items_list.insert(END, self.entry_item.get()) # insert into listbox
            self.model.insert_item(self.entry_item.get(), "") # insert into db
            self.entry_item.delete(0, END)

    # gets the current selected item
    def get_selected_item(self,event=None):
        try:
            #enables note
            self.note.config(state='normal')
            # loads the note text
            self.load_note(self.items_list.get(self.items_list.curselection()))
            # resets note border if not saved
            self.note.config(borderwidth=1)
            # sets current selected item text
            self.current_item = self.items_list.get(self.items_list.curselection())
            # returns current selected item [index]
            return self.items_list.curselection()[0]
        except IndexError:
            return None
        except:
            return None

    # when moving an item down in the index (with control + keyboard(DOWN))
    def move_item_down(self,event):
        current_item_index=self.get_selected_item(self)
        current_item_text = self.items_list.get(self.items_list.curselection())
        next_item_index=self.get_selected_item(self) + 1
        self.items_list.delete(current_item_index)
        self.items_list.insert(next_item_index,current_item_text)
        self.items_list_moved = True

    # when moving an item up in the index (with control + keyboard(UP))
    def move_item_up(self,event):
        current_item_index = self.get_selected_item(self)
        current_item_text = self.items_list.get(self.items_list.curselection())
        previous_item_index = self.get_selected_item(self) - 1

        self.items_list.delete(current_item_index)
        self.items_list.insert(previous_item_index, current_item_text)
        #selects the moved item
        self.items_list.activate(current_item_index)
        self.items_list_moved = True

    # when an index item is deleted with keyboard (DELETE)
    def delete_item(self,event):
        self.current_item = self.get_selected_item(event)
        if  self.current_item is not None:
            result = messagebox.askquestion("Delete","Delete item?")
            if result == "yes" and self.current_item is not None:
                current_item = self.items_list.get(self.items_list.curselection())
                self.model.delete_item(current_item)

                self.items_list.delete(self.current_item)
                self.entry_item.delete(0, END)

    # for new or update index items
    def insert_or_update_item(self,event):
        # if doubleclicked (edit mode)
        if self.item_edit_mode:
            self.items_list.delete(self.current_item)
            self.items_list.insert(self.current_item, self.entry_item.get())

            self.model.update_item(self.entry_item.get(),self.current_item_text)

            self.entry_item.delete(0, END)
            self.item_edit_mode = False
        # when new item (Entry keyboard INTRO)
        else:
            self.entry_new_item(event)

    # gets the updated item and updates it
    def get_edit_item(self,event):
        if self.get_selected_item() is not None:
            self.entry_item.delete(0, END)
            self.current_item_text = self.items_list.get(self.items_list.curselection()) # to store the old value if edited
            self.entry_item.insert(0,self.items_list.get(self.items_list.curselection()))

            self.current_item = self.get_selected_item(event)

            self.item_edit_mode = True

    # updates the item in db when changed position in listbox
    def update_item_position_db(self,event=None):
        if self.items_list_moved is True:
            all_items = self.items_list.get(0,END)
            self.model.update_item_postion(all_items)

        self.items_list_moved = None

        # loads corresponding note when item clicked
    def load_note(self, item):
        note_text = self.model.load_note(item)
        self.note.delete(1.0,END)
        self.note.insert(END, note_text)

    #updates note text in DB
    def update_note(self,event=None):
        text= self.note.get(1.0,END)
        try:
            self.model.update_note_text(text,self.current_item)
            self.note.config(borderwidth=1) # resets note border after save
        except:
            messagebox.showerror("Error","Please select an index item first!.")

    # changes note border if text changed to inform the user to save
    def note_text_changed(self,event=None):
        self.note.config(borderwidth = 10)











