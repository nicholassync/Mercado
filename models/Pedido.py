class Pedido:
    def __init__(self, cliente_id, produtoNome, quantidade, valor):
        self.__cliente_id = cliente_id
        self.__produtoNome = produtoNome
        self.__quantidade = quantidade
        self.__valor = valor

    def get_cliente_id(self):
        return self.__cliente_id

    def get_produto(self):
        return self.__produtoNome

    def get_quantidade(self):
        return self.__quantidade

    def get_valor(self):
        return self.__valor