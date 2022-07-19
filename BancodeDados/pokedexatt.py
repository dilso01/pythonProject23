import sqlite3

conexao = sqlite3.connect('Banco Pokemon.db')
cursor = conexao.cursor()


def criar():
    nome = input('Digito o nome: ')
    tipo = input('Digito o tipo: ')
    num_pokedex = input('Digito o num_pokedex: ')
    level = input('Digito o level: ')
    cursor.execute('INSERT INTO lista_pokemons(nome, tipo, num_pokedex, level)'
                   'VALUES(?, ?, ?, ?)', (nome, tipo, num_pokedex, level))
    conexao.commit()


def evoluir(a, b):
    cursor.execute('UPDATE lista_pokemons SET level=? WHERE pokedex=?', (a, b))
    conexao.commit()


def editar():
    cod_pokemon = int(input('Qual pokemon quer editar? '))
    lista = ['nome', 'tipo', 'pokedex']
    opcao = int(input('O que você quer editar?  [0] nome [1] tipo [2] pokedex'))
    novo_valor = input('Digite novo valor: ')

    cursor.execute(f'UPDATE lista_pokemons SET {lista[opcao]}="{novo_valor}" WHERE pokedex = {cod_pokemon}')

    conexao.commit()


def listar():
    cursor.execute('SELECT * FROM lista_pokemons')
    for pokedex in cursor.fetchall():
        print(f'{pokedex[0]} - {pokedex[1]} - {pokedex[2]} - {pokedex[3]} - {pokedex[4]}')


def deletar():
    cursor.execute('DELETE FROM lista_pokemons')
    conexao.commit()


editar()
listar()



cursor.close()
conexao.close()

