class Pessoa:
    def __init__(self):
        self.__nome = ""     
        self.__cpf = ""

    def get_nome(self):
        return self.__nome
    
    def get_Id(self):
        return self.__id

    def set_nome(self, nome):
        self.__nome = nome
           
    def set_cpf(self, cpf):
        self.__cpf = cpf
        
    def get_cpf(self):
        return self.__cpf
