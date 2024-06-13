from models.Pessoa import Pessoa


class Admin(Pessoa):
    def __init__( self ):
        super().__init__()
        self.__setor_de_trabalho = ""

    # Getter para setor_de_trabalho
    
    def Get_setor_de_trabalho(self):
        return self.__setor_de_trabalho

    # Setter para setor_de_trabalho
   
    def Set_setor_de_trabalho(self, valor):
        self.__setor_de_trabalho = valor

    

    