
class NoteBook:
    def __init__(self):
        self.full_path = "" # ie. c:/nb/myNotebook.snb
        self.path = "" # ie. c:/nb/
        self.name = "" #ie. myNoteBook
        self.name_ext = "" # ie. myNoteBook.snb

    def __name_splitter(self):
        # separa nombre
        name_tmp =self.full_path.split("/")
        self.name_ext = name_tmp[-1]

        name = self.name_ext.split(".")
        self.name = name[0]

        # separa ruta
        self.path = self.full_path.replace(self.name_ext,"")

    def set_nb_path(self,full_path):
        self.full_path = full_path
        self.__name_splitter()

    def get_nb_full_path(self):
        return self.full_path

    def get_nb_path(self):
        return self.path

    def get_nb_name(self):
        return self.name

    def get_nb_name_ext(self):
        return  self.name_ext

