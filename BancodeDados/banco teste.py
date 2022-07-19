import sqlite3
conexao = sqlite3.connect('Banco de dados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'cpf TEXT,'
               'nome TEXT,'
               'data_nascimento TEXT,'
               'cep TEXT,'
               'peso REAL,'
               'altura REAL)')
conexao.commit()


cpf = input('Digite cpf')
nome = input('Digite nome')
data_nascimento = input('Digite data nascimento')
cep = input('Digite cep')
peso = float(input('Digite peso'))
altura = float(input('Digite altura'))
cursor.execute('INSERT INTO clientes (cpf, nome, data_nascimento, cep, peso, altura)'
               'VALUES(?,?,?,?,?,?)', (cpf, nome, data_nascimento, cep, peso, altura))
conexao.commit()

cursor.execute('SELECT * FROM clientes')
for cliente in cursor.fetchall():
    print(f'{cliente[0]} - {cliente[1]} {cliente[2]} - {cliente[3]} - {cliente[4]} - {cliente[5]} - {cliente[6]}')

# cursor.execute('DELETE FROM clientes')
# conexao.commit()

cursor.close()
conexao.close()


