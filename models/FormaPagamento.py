from enum import Enum

class MetodoPagamento(Enum):
    DEBITO = 'Débito'
    CREDITO = 'Crédito'

class FormaPagamento:
    def __init__(self,id ,banco, metodo, valor, numero_cartao):
        self.__banco = banco
        self.__id = id
        self.__metodo = metodo  # Espera uma instância da enumeração MetodoPagamento
        self.__valor = valor
        self.__numero_cartao = numero_cartao

    def get_banco(self):
        return self.__banco

    def set_banco(self, banco):
        self.__banco = banco

    def get_metodo(self):
        return self.__metodo
    def get_Id(self):
        return self.__id
    
    def set_metodo(self, metodo):
        if isinstance(metodo, MetodoPagamento):
            self.__metodo = metodo
        else:
            raise ValueError("Método deve ser uma instância de MetodoPagamento.")

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor

    def get_numero_cartao(self):
        return self.__numero_cartao

    def set_numero_cartao(self, numero_cartao):
        self.__numero_cartao = numero_cartao