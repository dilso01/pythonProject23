# Código SKU

#Tipos de Produto:
print('1 - MON - Monitor')
print('2 - TEC - Teclado')
print('3 - MOU - Mouse')

cod1 = int(input('digite uma opção: '))
if cod1 == 1:
    cod = 'MON'
elif cod1 == 2:
    cod = 'TE'
elif cod1 == 3:
    cod = 'MOU'
if cod == 1:
    cod3 = 'Monitor'
elif cod == 2:
    cod3 = 'Teclado'
elif cod == 3:
    cod3 = 'Mause'

#print(cod, pro)
# Cor:
print('1 - PR - Preto')
print('2 - AZ - Azul')
print('3 - VM - Vermelho')
print('4 - BR - Branco')
cor1 = int(input('digite uma opção: '))
if cor1 == 1:
    cor = 'PR'
elif cor1 == 2:
    cor = 'AZ'
elif cor1 == 3:
    cor = 'VM'
elif cor1 == 4:
    cor = 'BR'
if cor == 1:
    cor3 = 'Preto'
elif cor == 2:
    cor3 = 'Azul'
elif cor == 3:
    cor3 = 'Vermalho'
elif cor == 4:
    cor3 = 'Branco'

#print(cod, cor)
# Material de Fabricação:
print('1 - PP = Polipropileno')
print('2 - PE = Polietileno')
print('3 - PO = Poliamida')
mat1 = int(input('digite uma opção: '))
if mat1 == 1:
    mat = 'PP'
elif mat1 == 2:
    mat = 'PE'
elif mat1 == 3:
    mat = 'PO'
if mat == 1:
    mat3 = 'Polipropileno'
elif mat1 == 2:
    mat3 = 'Polietileno'
elif mat1 == 3:
    mat3 = 'Poliamida'

#print(cod, cor, mat)
# Geração:
print('1 - 1G - 1ª Geração')
print('2 - 2G - 2ª Geração')
print('3 - 3G - 3ª Geração')
GE1 = int(input('digite uma opção: '))
if GE1 == 1:
    GE = '1G'
elif GE1 == 2:
    GE = '2G'
elif GE1 == 3:
    GE = '3G'
if GE1 == 1:
    ge3 = '1° Geração'
elif GE1 == 2:
    ge3 = '2° Geração'
elif GE1 == 3:
    ge3 = '3° Geração'

#print(cod, cor, mat, GE)

fab = input('Ano Cadastro: ')


modelo = (cod,cor,mat,GE,)
#print(modelo, sep='-', end='/')
print(cod3, cor3, 'de', mat3, fab, '=',cod,cor,mat,GE, sep='-', end='/')
print(fab)




# EXEMPLO:
# Mouse Branco de Poliamida 3ª Geração 2022 = MOU-BR-PO-3G/2022

# Criar um código que você pode cadastrar um produto, escolhendo as opções, e
# ao final ele traga o código, e que também possa digitar o código e ele trazer
# as informações
