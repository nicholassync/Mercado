from Logics import Logic
from Fuctions import Query
from models.Admins import Admin
from models.Cliente import Cliente
from models.Produto import Produto

admin = Admin
cliente = Cliente




decicao = int(input("(1) cliente (2) admin "))



def UserRole():
 admin = Logic.AdminOrCreateAdmin()

 while True:
    print("(1) para listagem\n(2) para edicao de produto\n(3) para criacao de um produto\n(4) para delecao de um produto\n(5) para sair")
    
    try:
        opcao = int(input("escolha uma decicao\n "))
    except ValueError:
        print("Por favor, insira apenas numero inteiros.")
        continue

    if opcao == 1:
        produtos = Query.GetAllProdutos()
        for produto in produtos:
            print(produto.nome)
        
    elif opcao == 2:
        Logic.UpdateProduto()
        # Aqui você colocaria a lógica para editar um produto

    elif opcao == 3:
        Logic.CreateProduto()
        # Aqui você colocaria a lógica para criar um produto

    elif opcao == 4:
        Logic.DeleteProduto()
        # Aqui você colocaria a lógica para deletar um produto

    elif opcao == 5:
        print("Saindo do programa...")
        break  # Encerra o loop

    else:
        print("Opcao invalida. Por favor, escolha uma Opcao valida.")
     
  
def ClienteRole():
  cliente = Logic.ClienteOrCreateCliente()
  carrinho = Logic.ListagemItensInsercaoDeProdutos()
  Logic.FinalizandoCompra(carrinho,cliente)
  while True:
    print("(1) para listagem de pedido \n(2)  edicao da conta \n(3) comprar novamente de um produto\n(4) para sair")
    opcao = int(input("escolha uma decicao\n "))
    
    if opcao == 1:
        pedidos = Query.GetAllPedidoOfCliente(cliente.id)
        for pedido in pedidos:
            print(f"nome do produto :{pedido.produto} , quantidade {pedido.quantidade}, custo total: {pedido.valor}\n")
        
    elif opcao == 2:
        Logic.FormularioUpdateCliente(cliente)
       
    elif opcao == 3:
        RestartBuy(cliente)       

    elif opcao == 4:
        break
       


def RestartBuy(cliente):
   carrinho = Logic.ListagemItensInsercaoDeProdutos()
   Logic.FinalizandoCompra(carrinho,cliente)
if(decicao == 1):
    ClienteRole()

if(decicao == 2):
    UserRole()
 