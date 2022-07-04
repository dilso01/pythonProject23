lista1 = list(range(5, 11))
lista2 = [3, 5, 7, 9, 3]

#transformar em set(conjunto)

set1 = set(lista1)
set2 = set(lista2)

if len(lista2) == len(set2):
    print('sem duplicadas')
else:
    print('Duplicadas')

#imprimir um set

print(f'set 1 {set1}')
print(f' set 2 {set2}')

set3 = {4, 5, 6, 8, 9}

print(type(set3))

# não e possivel alterar um item ja criado em set

# juntar 2 sets/ exclui os item repetidos
print(f'Union{set2.union(set1)}')

# interseção deixa somente o que nos dois set sao iguais

print(f'intersecao {set2.intersection((set1))}')

#diferença verifica a diferença fora da interseção
print(f'difference {set2.difference(set1)}')

#diferemca simétrica é o inverso da interseção
print(f'symmetric Difference {set2.symmetric_difference(set1)}')

#verificar se um item esta no set

if 9 in set2:
    print('encontrei')

#adicionar itens ao set

set2.add(25)
set1.add(14)
print(set1)
print(set2)

#adicionar uma lista ou tupla para um set

tupla1 = (3, 5, 13, 290)
lista3 = [260, 220, 240]

#set.update(tupla1)
print(set2)
# set.update(lista3)
print(set2)

#apagar um item - REMOVE

set.add(200)
print(set2)
set2.remove(200)
print(set2)

#metodo discard (ele não da erro se nao tiver o item)

set2.discard(230)
print(set2)

#usar o try para caso de erro e continuar rodar

# apagar o primeiro itm - pop

print(set2)
set2.pop()
print(set2)

#
set3 = set(range(1, 10))
print(set3)
set3.pop()
print(set3)

# para limpar o set
# set2.clear()
# print(set2)
# # print((type(set2)))
# set2 = {} #dessa maneira ele nao cria uma set, e uma dicionario, não é ideal usar

#laço no set
for i in set2:
    print(i)

