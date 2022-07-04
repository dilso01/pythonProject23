def triangulo(l1, l2, l3):
    if l1 + l2 < l3 or l2 + l3 < l1 or l1 + l3 < l2:
        return('Não é um triangulo')
    elif l1 == l2 == l3:
        return('Sim é um Triangulo Equilatero')
    elif l1 != l2 != l3:
        return ('Sim é um Triangulo Escaleno')
    else:
        return('Sim é um Triangulo Isóceles')


def contador(a,b):
    cont = 0
    for i in a:
        if i == b:
            cont += 1
    return cont


def inverso(a):
    a.reverse()
    return a


def jogada(a, b):
    if b == 0:
        if a == 0:
            return ('Empate')
        elif a == 1:
            return ('\033[0::36mJogador VENCE\033[0::36m')
        elif a == 2:
            return ('\033[0::36mJogador PERDEU\033[0::36m')
        else:
            return ('Jogada Inválida')

    elif b == 1:
        if a == 1:
            return ('Empate')
        elif a == 2:
            return ('\033[0::36mJogador VENCEU\033[0::36m')
        elif a == 0:
            return ('\033[0::36mJogador PERDEU\033[0::36m')
        else:
            return ('Jogada Inválida')

    elif b == 2:
        if a == 0:
            return ('\033[0::36mJogador VENCE\033[0::36m')
        elif a == 1:
            return ('\033[0::31mjogador PERDEU\033[0::31m')
        elif a == 2:
            return ('\033[0::31mEMPATE\033[0::31m')
        else:
            return ('Jogada Inválida')


