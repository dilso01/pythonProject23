'''
O DATAFOLGA, instituto de pesquisas, realizou uma pesquisas sobre as eleições de 2022. Porém os estagiários que fizeram a
pesquisa não conheciam o correto método de aplicar a pesquisa.
Acabaram gerando 2 arquivos TXT, onde cada um deles tem o CPF da intenção de voto das pessoas. Sabendo disso, mostre: quantos votos cada candidato ganhou.
>Qual foi o candidato que ganhou a eleição?
>Quantas pessoas votaram nos 2 candidatos?
>Quantas pessoas não votaram em nenhum dos candidatos? (existiam 100 eleitores)
>Assumindo que os que votaram nos 2 candidatos não serão contabilizados, quem seria o novo vencedor?
'''
candidato1 = open('Candidato A.txt','r').read().splitlines()
candidato2 = open('Candidato B.txt', 'r').read().splitlines()

print(len(candidato2))
print(len(candidato1))


# >Qual foi o candidato que ganhou a eleição?
if len(candidato2) > len(candidato1):
    print(' Candidato 2 Ganhou as elições')
elif len(candidato1) == len(candidato2):
    print('Empate')
else:
    print(' Candidato 1 Ganhou as elições')

set1 = set(candidato1)
set2 = set(candidato2)
# >Quantas pessoas votaram nos 2 candidatos?
totalV = len(candidato1) + len(candidato2)
print(f'Total de votos {totalV}')

print(f'Eleitores que votaram nos dois Candidatos {len(set2.intersection(set1))}')

# >Quantas pessoas não votaram em nenhum dos candidatos? (existiam 100 eleitores)
lista_completa = candidato2 + candidato1
total = (len(set(lista_completa)))
print(f' Eleitores que não votaram {100 - total}')
# >Assumindo que os que votaram nos 2 candidatos não serão contabilizados, quem seria o novo vencedor?

if len(set2) > len(set1):
    print(' Candidato 2 Ganhou as eleições')
elif len(set1) == len(set2):
    print('Empate')
else:
    print(' Candidato 1 Ganhou as eleições')
