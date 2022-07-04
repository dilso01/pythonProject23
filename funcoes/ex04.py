# Faça uma função que informe a quantidade de dígitos de um
# determinado número inteiro informado
# def contador(a):
#     cont = 0
#     for i in a:
#         cont += 1
#         return cont

def contador(a):
    cont = 0
    for i in str(a):
        cont += 1
    return cont


num = input('Informe o numero: ')
print(contador(num))