from note_panel import *
from index_panel import *
from tkinter import Menu

class View:
    def __init__(self,root):
        self.root = root
        self.note_panel = NotePanel(self.root)
        self.index_panel = IndexPanel(self.root)
        self.menu_bar = Menu(root)
        #

