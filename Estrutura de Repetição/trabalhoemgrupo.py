print(50*"-")
print('\33[93:40:2:1mVALIDADOR DE CPF\33[m'.center(60))
print(50*"-")

cpf = input('\33[93mInforme o cpf:\33[m').replace('.','').replace('-','').replace(',','')

while cpf == "00000000000" or cpf == '11111111111' or cpf == '22222222222' or cpf == '33333333333' or cpf == '44444444444' or cpf == '55555555555' or cpf == '66666666666' or cpf == '77777777777' or cpf == '888888888' or cpf == '99999999999':
    print(30 * "-")
    print('\33[31:40mCPF INVALIDO\33[m'.center(60))
    print(30 * "-")
    cpf = input('\33[31:40mCPF INVALIDO\33[m'.center(60)).replace('.','').replace('-','').replace(',','')
if cpf != len(cpf):
   print('\33[31:40mCPF INVALIDO\33[m'.center(60))
   cpf = input('\33[31:40mCPF INVALIDO\33[m'.center(60)).replace('.', '').replace('-', '').replace(',', '')
else:
   cpf = list(cpf)
   cont = 0
        contador = 10
        b = 0
    while contador >= 2:
        a = int(cpf[cont])
        b += a * contador
        contador = contador - 1
        cont = cont + 1

b = b % 11
b = 11 - b
pv1 = b

if b >= 10:
    b = 0
    pv1 = b
else:
    print()

cont = 0
contador = 11
b = 0

while contador >= 2:
    a = int(cpf[cont])
    b += a * contador
    contador = contador - 1
    cont = cont + 1

b = b % 11
b = 11 - b
pv2 = b

if b >= 10:
    b = 0
    pv2 = b
else:
    print()

if int(cpf[9]) == pv1 and int(cpf[10]) == pv2:
    print(50*"-")
    print('\33[32:40mCPF VÁLIDO\33[m'.center(60))
    print(50*"-")
else:
    print(50*"-")
    print('\33[31:40mCPF INVALIDO\33[m'.center(60))
    print(50*"-")