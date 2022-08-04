import sqlite3
from validate_docbr import CPF
import requests

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


#validar CPF

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

def validar_cpf(sera):
    cpf = CPF()
    cpf.validate(sera)
    if validar_cpf:
        print('CPF válido')
    else:
        print("CPF inválido")


def receber_dados_novo_produto():
    cod_barra = input('Digite o novo codigo de barra: ')
    nome_produto = input('Digete o nome do produto: ')
    fabricante_produto = input('Digite o nome do fabricante: ')
    if validar_cod_barra(cod_barra):
        if consultar_existencia_produto(cod_barra):
            p1 = Produto(cod_barra, nome_produto, fabricante_produto)
            p1.inserir_novo_produto()



def validar_cod_barra(codigo_barra):
    if len(codigo_barra) == 13:
        return True
    else:
        print('Código de barras precisa de 13 dígitos')
        return False


def consultar_existencia_produto(cod_barra):
    cursor.execute('SELECT * FROM produtos WHERE codigo_barras=?', (cod_barra,))
    resultado = cursor.fetchall()
    if len(resultado) != 0:
        print('Produto já existe')
        return False
    return True


def alterar_produto():
    codigo_barra_antigo = input('Digite o codigo de barra do produto que quer atualizar: ')
    codigo_barra_novo = input('Digite o novo código de barra: ')
    if validar_cod_barra(codigo_barra_novo):
        # if consultar_existencia_produto(codigo_barra_antigo):
        cursor.execute(f'UPDATE produtos SET codigo_barras=? WHERE codigo_barras=?', (codigo_barra_novo, codigo_barra_antigo))
        print('Modificação feita com sucesso')
        conexao.commit()


def excluir_produto():
    codigo_excluir = input('Digite o código do produto que deseja excluir: ')
    if codigo_excluir:
        cursor.execute('SELECT * FROM produtos WHERE codigo_barras=?', (codigo_excluir,))
        resultado = cursor.fetchall()
        if len(resultado) != 0:
            cursor.execute(f'DELETE FROM produtos WHERE codigo_barras=?', (codigo_excluir,))
            print('Produto excluido com sucesso')
            conexao.commit()
            return False
        return True



class Produto:
    def __init__(self, codigo_barra, nome_produto, fabricante_produto):
        self.codigo_barra = codigo_barra
        self.nome_produto = nome_produto
        self.fabricante_produto = fabricante_produto

    def inserir_novo_produto(self):
        cursor.execute('INSERT INTO produtos(codigo_barras, nome_produto, fabricante_produto)'
                       'VALUES(?, ?, ?)', (self.codigo_barra, self.nome_produto, self.fabricante_produto))
        print('Produto cadastrado com sucesso')
        conexao.commit()


    def excluir(self):
        codigo_barra = input('Digite o Codigo de barra que deseja excluir')
        cursor.execute(f'DELETE FROM produtos WHERE cpf_cliente="{codigo_barra}"')
        print('Produto excluido com sucesso')
        conexao.commit()


class Vendas:
    def __init__(self, cpf_cliente, cod_barra, quantidade, valor_unitario):
        self.cpf_cliente = cpf_cliente
        self.cod_barra = cod_barra
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario





def verificacao_cpf(a):
    v_cpf = a
    cpf = CPF()
    cpf.validate(v_cpf)
    if v_cpf:
        print('cpf valido')
    elif v_cpf == False:
        print("cpf invalido")


    # cursor.execute('INSERT INT vendas(cpf_clientes, cod_barra, quantidade, valor_unitario, valor_total)'
    #                'VALUES(?, ?, ?, ?, ?)', self.cpf_cliente, self.cod_barra, self.quantidade, self.valor_unitario, valor_total)
    # print('Venda Realizada com sucesso')
    # conexao.commit()



def memu():
    print('''O que deseja fazer?'
          '[1] para cadastrar cliente'
          '[2] para alterar'
          '[3] para excluir'
          '[4] para cadastrar um Produto'
          '[5] para alterar um Produto'
          '[6] para excluir um produto' 
          '[7] para fazer uma nova venda'
          '[8] para listar vendas por CPF'
          '[9] listar vendas por codigo de barras'
          '[10] Ranking de vendas por produto'
          '[11] Ranking de vendas por cliente'        
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
    elif opcao == 4:
        receber_dados_novo_produto()
    elif opcao == 5:
        alterar_produto()
    elif opcao == 6:
        excluir_produto()
    elif opcao == 7:
        nova_venda()
    elif opcao == 999:
        print("Finalizando o Sistema...")
        print('Programa finalizado')
        break


cursor.close()
conexao.close()



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
