from tkinter import Frame,Button

class NotePanel:
    def __init__(self,root):
        self.frame_note = Frame(root, bg="#f2ec9b")
        self.frame_note.grid(row=0,column=1,sticky="nsew")
