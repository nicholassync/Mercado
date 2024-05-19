class Carrinho:
    def __init__(self):
        self.__produtos = []

    def adicionar_produto(self, produto):
        self.__produtos.append(produto)

    def remover_produto(self, produto):
        self.__produtos.remove(produto)

    def listar_produtos(self):
        return self.__produtos

    def limpar_carrinho(self):
        self.__produtos = []