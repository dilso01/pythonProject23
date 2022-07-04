# Criar um algoritmo quantos números você desejar (laço infinito), e ao final dele mostre:
# A lista em ordem crescente
# A lista em ordem decrescente
# A soma de todos os itens
# A média de todos os números

laco = 'S'
lista = []
soma = 0
cont = 0

while 'S':
    if laco == 'S':
        num = int(input('Digite um número que deseja adicionar a lista: '))
        lista.append(num)
        soma += num
        num = 0
        cont += 1
        laco = input('deseja adicionar mais números?:''S ou N').upper()
    else:
        break
print(lista)
lista.sort
print(f'Sualista em ordem crescente é, {lista}')
lista.sort(reverse=True)
print(f'Sua lista em ordem decrescente é, {lista}')
print(f'A soma dos números da lista é, {soma}')
print(f'A média dos números digitados é {soma/cont}')

