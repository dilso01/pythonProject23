tupla1 = (3, 2, 4)
tupla2 = (8, [10, 3, 4,], 12)
print(type(tupla1))
''' voce cria uma tupla quando nao vai precisar ou nao quer adicionar nada'''
print(len(tupla1))
tupla1 += tupla2
tupla3 = (tupla1 + tupla2)
print(tupla3)
#posso colocar uma lista dentro de uma tupla, e a lista la dentro da tupla eu consigo alterar
tupla1[4][2] = 'Gaspar'
