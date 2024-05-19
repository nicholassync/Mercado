from models.Pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, id, email, totalCarteira):
        super().__init__(nome, id, cpf)
        self.__totalCarteira = totalCarteira

    def get_totalCarteira(self):
        return self.__totalCarteira

    def set_email(self, totalCarteira):
        self.__totalCarteiral = totalCarteira

