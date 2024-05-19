


class Pedido:
    def __init__(self, id ,cliente  , produtos, formapagamento):
        self.__cliente = cliente
        self.__id = id
        self.__produtos = produtos
        self.__formapagamento = formapagamento
        

    
    def set_formapagamento(self, formapagamento):
        self.__cliente = formapagamento

    def get_formapagamento(self):
        return self.formapagamento
    
    def get_cliente(self):
        return self.__cliente
    def get_Id(self):
        return self.__id

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def get_produtos(self):
        return self.__produtos

    def set_produtos(self, produtos):
        self.__produtos = produtos
    