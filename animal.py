# coding: utf-8

class Animal():
    """
        Model for Animal table in database
    """

    def __init__(self,
    ID, Name, IDType):
        """
            Constuctor   # reflet de ce qu'il y a dans la BDD
        """
        self.id = ID
        self.name = Name
        self.id_type = IDType