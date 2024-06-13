
from pyexpat import model
import pyodbc
from models.Admins import Admin
from models.Produto import Produto
from models.Cliente import Cliente
from models.Carrinho import Carrinho
from models.Pedido import Pedido
from Fuctions import Query
import os 

 
def DeleteProduto():
    produtos = Query.GetAllProdutos()
    count = 0
    for produto in produtos:
          count +=1 
          print(f"Código: {produto.codigo}, Nome: {produto.nome}, Preco: {produto.preco}, Posicao {count}")
    posicao = int(input("Posicao do produto que quer deletar"))
    produto = produtos[posicao -1]
    Query.DeleteProduto(produto.id)
    
def CreateProduto():
    produto = FormularioCreateProduto()
    Query.CreateProduto(produto.get_codigo(), produto.get_nome(), produto.get_preco(), produto.get_quantidade(), produto.get_setor(), produto.get_tipo())
def UpdateProduto():
     produtos = Query.GetAllProdutos()
     count = 0
     for produto in produtos:
          count +=1 
          print(f"Código: {produto.codigo}, Nome: {produto.nome}, Preco: {produto.preco}, "
              f"Quantidade: {produto.quantidade}, Setor: {produto.setor}, Tipo: {produto.tipo}, Posicao {count}")
     posicao = int(input("Posicao do produto"))
     produto = produtos[posicao - 1 ]
     entity = FormularioUpdateProduto(produto)
     Query.UpdateProduto(produto.id , entity.get_codigo(), entity.get_nome(), entity.get_preco(), entity.get_quantidade(), entity.get_setor(), entity.get_tipo() )
     
def FormularioUpdateCliente(clienteDb):
     cliente = Cliente() 
     novo_nome = input(f"Insira o nome do cliente (Atual: {clienteDb.nome}): ") or clienteDb.nome
     cliente.set_nome(novo_nome)

     novo_cpf = input(f"Insira o cpf do cliente (Atual: {clienteDb.cpf}): ") or clienteDb.cpf
     cliente.set_cpf(novo_cpf)

     novo_email = input(f"Insira o email do cliente (Atual: {clienteDb.email}): ") or clienteDb.email
     cliente.email(novo_email)
 
     nova_totalNaCarteira = input(f"Insira a total na carteira do cliente (Atual: {clienteDb.totalCarteira}): ") or clienteDb.totalCarteira
     cliente.total_carteira(nova_totalNaCarteira)

     
     Query.UpdateCliente(cliente.Getid(), cliente.Getnome(),cliente.get_cpf(),cliente.Getemail(),cliente.Gettotal_carteira())
     


def FormularioUpdateProduto(produtoDb):
    produto = Produto()
    
    novo_codigo = input(f"Insira o código do produto (Atual: {produtoDb.codigo}): ") or produtoDb.codigo
    produto.set_codigo(novo_codigo)

    novo_nome = input(f"Insira o nome do produto (Atual: {produtoDb.nome}): ") or produtoDb.nome
    produto.set_nome(novo_nome)

    novo_preco = input(f"Insira o preço do produto (Atual: R${produtoDb.preco}): ") or produtoDb.preco
    produto.set_preco(novo_preco)

    nova_quantidade = input(f"Insira a quantidade do produto (Atual: {produtoDb.quantidade}): ") or produtoDb.quantidade
    produto.set_quantidade(nova_quantidade)

    novo_setor = input(f"Insira o setor do produto (Atual: {produtoDb.setor}): ") or produtoDb.setor
    produto.set_setor(novo_setor)

    novo_tipo = input(f"Insira o tipo do produto (Atual: {produtoDb.tipo}): ") or produtoDb.tipo
    produto.set_tipo(novo_tipo)

    # Chamada de função de atualização (supondo que exista uma função para atualizar produtos no banco)
    return produto

def FormularioCreateProduto():
     produto = Produto() 
     novo_codigo = input(f"Insira o codigo do produto : ") 
     produto.set_codigo(novo_codigo)

     novo_nome = input(f"Insira o nome do produto: ") 
     produto.set_nome(novo_nome)

     novo_preco = input(f"Insira o preço do produto : ") 
     produto.set_preco(novo_preco)
 
     nova_quantidade = input(f"Insira a quantidade do produto : ") 
     produto.set_quantidade(nova_quantidade)

     novo_setor = input(f"Insira o setor do produto : ") 
     produto.set_setor(novo_setor)

     novo_tipo = input(f"Insira o tipo do produto : ") 
     produto.set_tipo(novo_tipo)

     return produto

def AdminOrCreateAdmin():
    Decisao = int(input("Se ja tiver cadastro, digite 1. Caso nao tenha, digite 2:\n"))   
    if Decisao == 1:
        cpf = input("Digite seu CPF:\n")
        admin  = ValidadeAdmin(cpf) 
        return admin
    else:
        admin = CreateAdmin()
        return admin
    
def ClienteOrCreateCliente():
    Decisao = int(input("Se ja tiver cadastro, digite 1. Caso nao tenha, digite 2:\n"))   
    if Decisao == 1:
        cpf = input("Digite seu CPF:\n")
        cliente  = ValidadeCliente(cpf) 
        if cliente is None:
             CreateUser()
        return cliente
    else:
        cliente = CreateUser()
        return cliente
    
def ListagemItensInsercaoDeProdutos():
    Itens = Query.GetAllProdutos()
    carrinho = []  # Carrinho inicializado como uma lista vazia
    count = 0

    while True:
        decisao = int(input("Quer inserir ou remover um item no carrinho (1 para inserir, 2 para remover)?\n"))
        if decisao == 1:
            for item in Itens:
                print(item.nome, count)
                count += 1

            try:
                itemPosition = int(input("Por favor, digite o número que está à direita do produto para selecioná-lo: "))
                
                if 0 <= itemPosition < len(Itens):
                    carrinho.append(Itens[itemPosition])
                    Itens[itemPosition].quantidade -= 1
                    if Itens[itemPosition].quantidade == 0:
                        Itens.pop(itemPosition)
                    count = 0
                else:
                    print("Posição inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.\n")
                continue

        elif decisao == 2:
            for idx, item in enumerate(carrinho):
                print(f"{idx}. {item.nome}")

            try:
                itemPosition = int(input("Por favor, escolha o número do item que deseja remover do carrinho:\n"))
                
                if 0 <= itemPosition < len(carrinho):
                    carrinho.pop(itemPosition)
                    count = 0
                else:
                    print("Posição inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.\n")
                continue

        try:
            validate = int(input("Deseja Sair (1), Adicionar mais no carrinho (2): \n"))
            if validate == 1:
                return carrinho
                os.system('cls') 
                
        except ValueError:
            print("Entrada inválida. Saindo do loop.")
            break
           

def RemocaoDoCarrinho(carrinho:list):
    print


def FinalizandoCompra(carrinho: list , cliente):
    produtoAtual = 0
    count = 0 
    while carrinho:
     for itens in carrinho:
       if(itens.id == produtoAtual):
         carrinho.pop(count)
         
         
       else:        
        produtoAtual = itens.id
        quantidadeDoProdutoNaBase = itens.quantidade
        quantidadeComprada =  quantidadeComprada = sum(1 for item in carrinho if item.nome == item.nome)  ##carrinho.count(where nome == item.nome)
        valor = itens.preco * quantidadeComprada
        clienteId = cliente.id
        pedido = Pedido(clienteId, itens.nome,quantidadeComprada, valor )
        carrinho.pop(count)
        Query.createPedidoAndAttBase(pedido,quantidadeComprada)             
                          
def ValidadeCliente(cpf:str):

    user = Query.GetClienteByCpf(cpf)
    if user is not None:
        return user
    else:
        print("Usuario Não encontrado")
        print("Deseja Tentar Novamente?\n 1: Sim , 2: Não")
        IsRetryTentativa =  int(input("Por favor, insira um número inteiro: "))
        if IsRetryTentativa == 1:
            cpfretry  = input("Digite seu CPF:\n")
            ValidadeCliente(cpfretry)
        else:
            ## retornar e sair do metodo 
            return

def ValidadeAdmin(cpf:str):

    user = Query.GetAdminByCpf(cpf)
    if user is not None:
        return user
    else:
        print("Usuario Não encontrado")
        print("Deseja Tentar Novamente?\n 1: Sim , 2: Não")
        IsRetryTentativa =  int(input("Por favor, insira um número inteiro: "))
        if IsRetryTentativa == 1:
            cpfretry  = input("Digite seu CPF:\n")
            ValidadeAdmin(cpfretry)
        else:
            ## retornar e sair do metodo 
            return


def CreateAdmin(): ##retornar o cliente aqui
    admin = Admin()
        
    admin.set_nome(str(input("Por favor, insira o seu nome: ")))
    admin.set_cpf(str(input("Por favor, insira o seu cpf: ")))
    admin.Set_setor_de_trabalho(str(input("Por favor, insira o seu Setor de trabalho: ")))
    adminDb = Query.CreateAdmin(admin.get_nome(), admin.get_cpf(), admin.Get_setor_de_trabalho())
    CreateEnderecoAdmin(adminDb)
    return adminDb
def CreateUser(): ##retornar o cliente aqui
    cliente = Cliente()
    cliente.set_nome(str(input("Por favor, insira o seu nome: ")))
    cliente.total_carteira(int(input("Por favor, insira a quantidade na carteira: ")))
    cliente.set_cpf(str(input("Por favor, insira o seu cpf: ")))
    cliente.email(str(input("Por favor, insira o seu email: ")))
    
    clientedb = Query.CreateCliente(cliente.get_nome(),cliente.get_cpf(),cliente.Getemail(),cliente.Gettotal_carteira())
    
    CreateEnderecoCliente(clientedb)
    return clientedb


def CreateEnderecoAdmin(adminDb):
    rua = input("Digite a rua: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    cep = input("Digite o CEP: ")   
    admin_id = adminDb.id
    Query.CreateEnderecoAdmin(rua,cidade, estado,cep, admin_id)

def CreateEnderecoCliente(clienteDb):
    rua = input("Digite a rua: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    cep = input("Digite o CEP: ")
    cliente_id = clienteDb.id
    Query.CreateEnderecoCliente(rua,cidade, estado,cep, cliente_id)

# Executando a consulta com o uso expl�cito de text para SQL direto

   ## result = connection.execute('SELECT * FROM Cliente')  # Ajuste o nome da tabela se necess�rio 
# try:
#     result = 'INSERT INTO Admin (id, cpf, nome, setor_de_trabalho, endereco_id) VALUES (?, ?, ?, ?, ?)'
    
#     # Valores a serem inseridos na tabela Admin
#     values = (5, '52888950820', '', '', 1)
    
#     # Executa a consulta de inserção
#     connection.execute(result, values)
    
#     # Confirma as mudanças no banco de dados
#     connection.commit()
    
# except e :
#     print(f"Erro ao executar a consulta: {e}")
#     pass
# # Fechar a conexão se não for mais necessária


##connection.close()
