cpf = 12345678936
if cpf == "00000000000" or '11111111111' or '22222222222' or '33333333333' or '44444444444' or '55555555555' or '66666666666' or '77777777777' or '888888888' or '99999999999':
    cpf = 'oxi'
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
    if int(cpf[9]) == pv1 and int(cpf[10]) == pv2:
        cpf = 'VÁLIDO'
    else:
        cpf = 'INVÁLIDO'
print(cpf)