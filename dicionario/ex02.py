# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde estes resultados em um dicionário.
# No final, coloque o dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.
from operator import itemgetter
from random import randint

dic = {}

for i in range(1,6):
    dic[f'jogaor{i}'] = randint(1,6)

ganhador = sorted(dic.items(), key=itemgetter(1), reverse=True)
print(ganhador)
