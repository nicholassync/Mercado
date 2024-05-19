class Endereco:
    def __init__(self,id, rua, cidade, estado, cep):
        self.__id = id
        self.__rua = rua
        self.__cidade = cidade
        self.__estado = estado
        self.__cep = cep

    def get_rua(self):
        return self.__rua
    def get_Id(self):
        return self.__id

    def set_rua(self, rua):
        self.__rua = rua

    def get_cidade(self):
        return self.__cidade

    def set_cidade(self, cidade):
        self.__cidade = cidade

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def get_cep(self):
        return self.__cep

    def set_cep(self, cep):
        self.__cep = cep