import pyodbc
from models.Pedido import Pedido

connection_string = (
    "Driver={SQL Server};"
    "Server=DESKTOP-6ARRAEL;"
    "Database=MercadoDb;"
)

# CRUD for Cliente
def CreateCliente(nome, cpf, email, total_carteira):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        # Insere o cliente e recupera o ID na mesma operação, como no método CreateAdmin
        insert_query = """
        INSERT INTO Cliente (nome, cpf, email, totalCarteira) 
        OUTPUT INSERTED.id
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(insert_query, (nome, cpf, email, total_carteira))
        id_cliente = cursor.fetchone()[0]  # Pega o ID do cliente inserido

        # Recupera todos os dados do cliente inserido
        cursor.execute("SELECT * FROM Cliente WHERE id = ?", (id_cliente,))
        cliente = cursor.fetchone()
        conn.commit()  # Garante que o INSERT foi concluído após a leitura dos dados

        return cliente

def GetClienteByCpf(cpf):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cliente WHERE cpf = ?", (cpf,))
        return cursor.fetchone()

def GetAdminByCpf(cpf):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Admin WHERE cpf = ?", (cpf,))
        return cursor.fetchone()

def GetAllClientes():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cliente")
        return cursor.fetchall()

def GetClienteById(cliente_id):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cliente WHERE id = ?", (cliente_id,))
        return cursor.fetchone()

def UpdateCliente(cliente_id, nome, cpf, email, total_carteira):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Cliente SET nome = ?, cpf = ?, email = ?, totalCarteira = ? WHERE id = ?", (nome, cpf, email, total_carteira, cliente_id))
        conn.commit()

def DeleteCliente(cliente_id):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Cliente WHERE id = ?", (cliente_id,))
        conn.commit()

# CRUD for Admin
def CreateAdmin(nome, cpf, setor_de_trabalho):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        # Supondo que a coluna de ID seja chamada 'id' e seja autoincrementada
        insert_query = """
        INSERT INTO Admin (nome, cpf, setor_de_trabalho) 
        OUTPUT INSERTED.id
        VALUES (?, ?, ?)
        """
        cursor.execute(insert_query, (nome, cpf, setor_de_trabalho))
        id_admin = cursor.fetchone()[0]  # Pega o ID do admin inserido

        # Recupera todos os dados do admin inserido
        cursor.execute("SELECT * FROM Admin WHERE id = ?", (id_admin,))
        admin = cursor.fetchone()
        conn.commit()  # Garante que o INSERT foi concluído após a leitura dos dados

        return admin

def GetAllAdmins():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Admin")
        return cursor.fetchall()

def GetAdminById(admin_id):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Admin WHERE id = ?", (admin_id,))
        return cursor.fetchone()

def UpdateAdmin(admin_id, nome, cpf, setor_de_trabalho):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Admin SET nome = ?, cpf = ?, setor_de_trabalho = ? WHERE id = ?", (nome, cpf, setor_de_trabalho, admin_id))
        conn.commit()

def DeleteAdmin(admin_id):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Admin WHERE id = ?", (admin_id,))
        conn.commit()

# CRUD for Endereco
def CreateEnderecoAdmin(rua, cidade, estado, cep, adminId):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        # Preparação da consulta SQL com a inclusão de clienteId e adminId
        
        # Execução da consulta com todos os parâmetros
        cursor.execute("INSERT INTO Endereco (rua, cidade, estado, cep, clienteId, adminId) VALUES (?, ?, ?, ?, ?, ?)", (rua, cidade, estado, cep, None, adminId))
        conn.commit()

def CreateEnderecoCliente(rua, cidade, estado, cep, clienteId):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        # Preparação da consulta SQL com a inclusão de clienteId e adminId
        
        # Execução da consulta com todos os parâmetros
        cursor.execute("INSERT INTO Endereco (rua, cidade, estado, cep, clienteId, adminId) VALUES (?, ?, ?, ?, ?, ?)", (rua, cidade, estado, cep, clienteId, None))
        conn.commit()
def GetAllEnderecos():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Endereco")
        return cursor.fetchall()

def GetEnderecoById(endereco_id):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Endereco WHERE id = ?", (endereco_id,))
        return cursor.fetchone()

def UpdateEndereco(endereco_id, rua, cidade, estado, cep):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Endereco SET rua = ?, cidade = ?, estado = ?, cep = ? WHERE id = ?", (rua, cidade, estado, cep, endereco_id))
        conn.commit()

def DeleteEndereco(endereco_id):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Endereco WHERE id = ?", (endereco_id,))
        conn.commit()

# CRUD for FormaPagamento
def CreateFormaPagamento(banco, metodo, valor, numero_cartao):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO FormaPagamento (banco, metodo, valor, numero_cartao) VALUES (?, ?, ?, ?)", (banco, metodo, valor, numero_cartao))
        conn.commit()

def GetAllFormasPagamento():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM FormaPagamento")
        return cursor.fetchall()

def GetFormaPagamentoById(formapagamento_id):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM FormaPagamento WHERE id = ?", (formapagamento_id,))
        return cursor.fetchone()

def UpdateFormaPagamento(formapagamento_id, banco, metodo, valor, numero_cartao):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE FormaPagamento SET banco = ?, metodo = ?, valor = ?, numero_cartao = ? WHERE id = ?", (banco, metodo, valor, numero_cartao, formapagamento_id))
        conn.commit()

def DeleteFormaPagamento(formapagamento_id):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM FormaPagamento WHERE id = ?", (formapagamento_id,))
        conn.commit()
def CreateProduto(codigo, nome, preco, quantidade, setor, tipo):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Produto (codigo, nome, preco, quantidade, setor, tipo) VALUES (?, ?, ?, ?, ?, ?)", (codigo, nome, preco, quantidade, setor, tipo))
        conn.commit()

def GetAllProdutos():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produto")
        return cursor.fetchall()

def GetProdutoById(produto_id):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produto WHERE id = ?", (produto_id,))
        return cursor.fetchone()

def UpdateProduto(produto_id, codigo, nome, preco, quantidade, setor, tipo):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Produto SET codigo = ?, nome = ?, preco = ?, quantidade = ?, setor = ?, tipo = ? WHERE id = ?", (codigo, nome, preco, quantidade, setor, tipo, produto_id))
        conn.commit()

def DeleteProduto(produto_id):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Produto WHERE id = ?", (produto_id,))
        conn.commit()
        
# CRUD for Pedido
def create_pedido(cliente_id, produto, quantidade, valor):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Pedido (cliente_id, produto, quantidade, valor) VALUES (?, ?, ?, ?)", 
                       (cliente_id, produto, quantidade, valor))
        conn.commit()

def createPedidoAndAttBase(pedido : Pedido , quantidade):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Pedido (cliente_id, produto, quantidade, valor) VALUES (?, ?, ?, ?)", 
                       (pedido.get_cliente_id(), pedido.get_produto(), pedido.get_quantidade(), pedido.get_valor()))
        
        # Atualize a quantidade de produtos no estoque
        cursor.execute("UPDATE Produto SET quantidade = quantidade - ? WHERE nome = ?",
                       (quantidade, pedido.get_produto()))
        conn.commit()

# Read Pedido
def GetAllPedido():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Pedido")
        return cursor.fetchone()

def GetAllPedidoOfCliente(clienteId):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Pedido WHERE cliente_id = ?",(clienteId))
        return cursor.fetchall()

def GetPedidoById(pedido_Id):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Pedido WHERE id = ?", (pedido_Id,))
        return cursor.fetchone()
 
# Update Pedido
def update_pedido(pedido_id, cliente_id, produto, quantidade, valor):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Pedido SET cliente_id=?, produto=?, quantidade=?, valor=? WHERE id=?", 
                       (cliente_id, produto, quantidade, valor, pedido_id))
        conn.commit()

# Delete Pedido
def delete_pedido(pedido_id):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Pedido WHERE id=?", (pedido_id,))
        conn.commit()