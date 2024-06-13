class Carrinho:
    def __init__(self):
        self.__produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def listar_produtos(self):
        return self.produtos

    def limpar_carrinho(self):
        self.produtos = []