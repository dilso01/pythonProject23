import sqlite3

conexao = sqlite3.connect('vendas.db')
cursor = conexao.cursor()

class Cliente:
    def __init__(self, nome, cpf_cliente, cep_cliente, cidade_cliente, estado_cliente, rua_cliente):
        self.nome = nome
        self.cpf_cliente = cpf_cliente
        self.cep_cliente = cep_cliente
        self.cidade_cliente = cidade_cliente
        self.estado_cliente = estado_cliente
        self.rua_cliente = rua_cliente


    def alterar_nome(self, antigo, novo):


        cursor.execute(f'UPDATE clientes SET nome_cliente= "{novo}" WHERE nome_cliente="{antigo}"')



#cadastrar novos dados
def novo_cliente():
    nome = input('Digite o nome: ')
    cpf_cliente = int(input('Digite o CPF: '))
    cep_cliente = input('Digite o cep: ')

    cursor.execute('INSERT INTO clientes(nome, cpf_cliente, cep_cliente, cidade_cliente, estado_cliente, rua_cliente)'
                   'VALUES(?, ?, ?, " ", " ", " ")', (nome, cpf_cliente, cep_cliente))

    conexao.commit()


def novo_produto():
    codigo_barra = input('Digite o codigo de barra: ')
    nome_prudoto = int(input('Digite o nome do produto: '))
    fabricante_produto = input('Digite o fabricante produto: ')
    cursor.execute('INSERT INTO produto(codigo_barra, nome_produto, fabricante_produto)'
                   'VALUES(?, ?, ?, ?)', (codigo_barra, nome_prudoto, fabricante_produto))
    conexao.commit()

def nova_venda():
    data_venda = input('Digite o nome: ')
    hora_venda = input('Digite o CPF: ')
    cpf_cliente = input('Digite o CPF: ')
    codigo_barra = input('Digite a cidade: ')
    quantidade = float(input('Digite a Quantidade: '))
    valor_unitario = float(input('Digite o valor: '))
    valor_total = valor_unitario * quantidade


    cursor.execute('INSERT INTO lista_pokemons(data_venda, hora_venda, cpf_cliente, codigo_barra, quantidade, valor_unitario, valor_total)'
                   'VALUES(?, ?, ?, ?)', (data_venda, hora_venda, cpf_cliente, codigo_barra, quantidade, valor_unitario, valor_total))
    conexao.commit()


#alterar registro

