from models.Pessoa import Pessoa
from models.Endereco import Endereco

class Cliente(Pessoa):
    def __init__(self):
        super().__init__()  # Chama o construtor da classe base
        self.__nome = ''
        self.__email = ''
        self.__total_carteira = 0
        self.__id = 0
        ## self.Endereco = Endereco()
       # Getter para nome
     
    def Getid(self):
        return self.__id

    # Setter para nome
   
    def Setid(self,id):
        self.__id= id
    def Getnome(self):
        return self.__nome

    # Setter para nome
   
    def Setnome(self,valor):
        self.__nome = nome

    # Getter para email
    
    def Getemail(self):
        return self.__email

    # Setter para email
    
    def email(self , valor):
        self.__email = valor

    # Getter para total_carteira
    
    
    def Gettotal_carteira(self):
        return self.__total_carteira

    
    def total_carteira(self, valor):
        self.__total_carteira = valor