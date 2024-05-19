class Pessoa:
    def __init__(self, nome, id, cpf):
        self.__nome = nome
        self.__id = id
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome
    
    def get_Id(self):
        return self.__id

    def set_nome(self, nome):
        self.__nome = nome

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id
        
    def set_cpf(self, cpf):
        self.__cpf = cpf
        
    def get_cpf(self):
        return self.__cpf
