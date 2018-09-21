from tkinter import Frame,Text,Scrollbar
from  tkinter.font import Font

class NotePanel:
    def __init__(self,root):
        self.frame_note = Frame(root, bg="#f2ec9b")
        self.frame_note.grid(row=0,column=1,sticky="nsew")
        self.frame_note.columnconfigure(0,weight=1)
        self.frame_note.rowconfigure(0,weight=1)

        self.note_text = Text(self.frame_note,bg='#ffff99',font=Font(family="Sans Serif", size=11),state='disabled')
        self.note_text.grid(row=0,column=0,sticky="nsew")

        scroll_vertical = Scrollbar(self.frame_note, command=self.note_text.yview)
        scroll_vertical.grid(row=0, column=1, sticky="nsew")
        self.note_text.config(yscrollcommand=scroll_vertical.set)
