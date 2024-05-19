from models.Pessoa import Pessoa


class Admin(Pessoa):
    def __init__(self, nome, id, setor_de_trabalho, ):
        super().__init__(nome, id)
        self.__setor_de_trabalho = setor_de_trabalho

    

    