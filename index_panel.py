from tkinter import Frame,Entry,Checkbutton,Listbox,Scrollbar
from  tkinter.font import Font

class IndexPanel:
    def __init__(self,root):
        self.frame_index = Frame(root, bg="#bdcfed")
        self.frame_index.grid(row=0, column=0,sticky="nsew")
        self.frame_index.rowconfigure(1, weight=1)

        ############################################# tools frame
        self.frame_tools = Frame(self.frame_index,bg="#9bbbf2")
        self.frame_tools.grid(row=0,column=0,sticky="nsew")

        self.entry = Entry(self.frame_tools,state='disabled',width=25)
        self.entry.grid(row=0,column=0,padx=8,pady=8,sticky="w")

        self.chk_is_section = Checkbutton(self.frame_tools,text="Is section",bg="#9bbbf2",state='disabled')
        self.chk_is_section.grid(row=0,column=1,padx=8,pady=8,sticky="w")

        ############################################# index items frame
        self.frame_items_index = Frame(self.frame_index,bg="#bdcfed")
        self.frame_items_index.grid(row=1, column=0,sticky="nsew")
        self.frame_items_index.columnconfigure(0,weight=1)
        self.frame_items_index.rowconfigure(0,weight=1)

        self.items_list = Listbox(self.frame_items_index, borderwidth=0, highlightthickness=0,
                                  font=Font(family="Sans Serif", size=11),bg="#bdcfed")
        self.items_list.grid(row=0,column=0,padx=5,pady=5,sticky='nsew')

        scroll_vertical = Scrollbar(self.frame_items_index, command=self.items_list.yview)
        scroll_vertical.grid(row=0, column=1, sticky="nsew")
        self.items_list.config(yscrollcommand=scroll_vertical.set)



