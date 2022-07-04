'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
linha = ('-='*15)
print(linha)
print('Vamos verificar o seu aproveitamoento')
print(linha)
dic = {'nome' : input('digite o nome: '),
      'N.Partidas': int(input('numeor de parditas: '))}
total = 0
for i in range(dic['N.Partidas']):
    dic[f'Partida{i}'] = golsP = int(input('Digite o número de gols em cada partida: '))
    total += golsP

dic['total de gols no Camp'] = total
print(dic)