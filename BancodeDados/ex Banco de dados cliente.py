import sqlite3

conexao = sqlite3.connect('vendas.db')
cursor = conexao.cursor()

class Cliente:
    def __init__(self, nome, cpf_cliente, cep_cliente):
        self.nome = nome
        self.cpf_cliente = cpf_cliente
        self.cep_cliente = cep_cliente
        self.cidade_cliente = "None"
        self.estado_cliente = "None"
        self.rua_cliente = "None"

#Alterar
    def alterar(self, cpf, novo_cpf, opcao):


        cursor.execute(f'UPDATE clientes SET {lista[opcao]}= "{novo_cpf}" WHERE cpf_cliente="{cpf}"')
        print('Modificação feita com sucesso')
        conexao.commit()

#cadastrar novos dados
    def novo_cliente(self):
        cursor.execute('INSERT INTO clientes(nome_cliente, cpf_cliente, cep_cliente, cidade_cliente, estado_cliente, '
                       'rua_cliente) '
                       'VALUES(?, ?, ?, ?, ?, ?)', (self.nome, self.cpf_cliente, self.cep_cliente, self.cidade_cliente, self.estado_cliente, self.rua_cliente))
        print('Cliente cadastrado com sucesso')
        conexao.commit()

#excluir
    def excluir(self):
        cpf = input('Digite o CPF que deseja excluir')
        cursor.execute(f'DELETE FROM clientes WHERE cpf_cliente="{cpf}"')
        print('Cliente excluido com sucesso')
        conexao.commit()





class Produto:
    def __init__(self, codigo_barra, nome_produto, fabricante_produto):
        self.codigo_barra = codigo_barra
        self.nome_produto = nome_produto
        self.fabricante_produto = fabricante_produto


    def novo_produto(self):
        cursor.execute('INSERT INT produtos(codigo_barra, nome_produto, fabricante_produto)'
                       'VALUES(?, ?, ?)', (self.codigo_barra, self.nome_produto, self.fabricante_produto))
        print('Produto cadastrado com sucesso')
        conexao.commit()


    def excluir(self):
        codigo_barra = input('Digite o Codigo de barra que deseja excluir')
        cursor.execute(f'DELETE FROM produtos WHERE cpf_cliente="{codigo_barra}"')
        print('Produto excluido com sucesso')
        conexao.commit()



def memu():
    print('''O que deseja fazer?'
          '[1] para cadastrar cliente'
          '[2] para alterar'
          '[3] para excluir'
          '[4] para cadastrar um Produto'
          '[5] para alterar um Produto'
          '[6] para excluir um produto'         
          [999] para finalizar o programa''')


while True:
    memu()
    opcao = int(input('Digite o que deseja fazer: '))
    if opcao == 1:
        nome = input('Digite o nome: ')
        cpf_cliente = input('Digite o cpf: ')
        cep_cliente = input('Digite o CEP: ')
        c1 = Cliente(nome, cpf_cliente, cep_cliente)
        c1.novo_cliente()
    elif opcao == 2:
        cpf = input('Digite seu cpf: ')
        lista = ['nome_cliente', 'cpf_cliente', 'cep_cliente']
        opcao = int(input('O que você quer editar?  [0] nome [1] cpf_cliente [2] cep_cliente'))
        novo_cpf = input('Digite o novo valor: ')
        c1 = Cliente(cpf, novo_cpf, opcao)
        c1.alterar(cpf, novo_cpf, opcao)
    elif opcao == 3:
        c1 = Cliente
        c1.excluir(opcao)
    elif opcao == 999:
        print("Finalizando o Sistema...")
        print('Programa finalizado')
        break









cursor.close()
conexao.close()


# def novo_produto():
#     codigo_barra = input('Digite o codigo de barra: ')
#     nome_prudoto = int(input('Digite o nome do produto: '))
#     fabricante_produto = input('Digite o fabricante produto: ')
#     cursor.execute('INSERT INTO produto(codigo_barra, nome_produto, fabricante_produto)'
#                    'VALUES(?, ?, ?, ?)', (codigo_barra, nome_prudoto, fabricante_produto))
#     conexao.commit()
#
# def nova_venda():
#     data_venda = input('Digite o nome: ')
#     hora_venda = input('Digite o CPF: ')
#     cpf_cliente = input('Digite o CPF: ')
#     codigo_barra = input('Digite a cidade: ')
#     quantidade = float(input('Digite a Quantidade: '))
#     valor_unitario = float(input('Digite o valor: '))
#     valor_total = valor_unitario * quantidade
#
#
#     cursor.execute('INSERT INTO lista_pokemons(data_venda, hora_venda, cpf_cliente, codigo_barra, quantidade, valor_unitario, valor_total)'
#                    'VALUES(?, ?, ?, ?)', (data_venda, hora_venda, cpf_cliente, codigo_barra, quantidade, valor_unitario, valor_total))
#     conexao.commit()
