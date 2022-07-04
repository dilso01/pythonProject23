# Crie um algoritmo que receba quantos nomes(apenas nome) desejar, e ao final:
# A lista em ordem crescente
# A lista em ordem decrescente
# O total de nomes cadastrados
# Quantos ‘Carlos’ existem na lista

laco = 'S'
lista = []

cont = 0

while 'S':
    if laco == 'S':
        nome = input('Digite um número que deseja adicionar a lista: ')
        lista.append(nome)
        nome = 0
        cont += 1
        laco = input('deseja adicionar mais números?:''S ou N').upper()
    else:
        break
print(lista)
lista.sort()
print(f'lista em ordem alfabetica {lista}')
lista.sort(reverse=True)
print(f'lista em ordem alfabetica decrescente {lista}')
print(f'Quabtidade de nomes cadastrados é, {cont}')
print(f'Quantidade de Carlos na lista é', lista.count('carlos'))