import sqlite3

conexao = sqlite3.connect('Meu primeiro banco.db')
cursor = conexao.cursor()
#
# #criar tabela
# cursor.execute('CREATE TABLE IF NOT EXISTS frutas('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
#                'nome_fruta TEXT,'
#                'variedade TEXT)')
# conexao.commit()
#
# #inserir dados na tabela - C
# cursor.execute('INSERT INTO frutas(nome_fruta, variedade)'
#                'VALUES("Banana","Caturra")')
# conexao.commit()



# #Atualizar registro - U
# cursor.execute('UPDATE frutas SET variedade="Branca"WHERE id=3')
# conexao.commit()
#
# #Deletar
# cursor.execute('DELETE FROM frutas')
# conexao.commit()



# # #Buscar dados - R
# cursor.execute('SELECT * FROM frutas')
# for fruta in cursor.fetchall():
#     print(f'{fruta[0]} - {fruta[1]} - {fruta[2]}')
#
# #deletar tabela
# cursor.execute('DROP TABLE frutas')
# conexao.commit()


cursor.close()
conexao.close()