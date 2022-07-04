from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')


def jogada(a):
    if computador == 0:
        if jogador == 0:
            return ('Empate')
        elif jogador == 1:
            return ('\033[0::36mJogador VENCE\033[0::36m')
        elif jogador == 2:
            if jogador == 0:
                return ('\033[0::31mjogador PERDEU\033[0::31m')
        else:
            return ('Jogada Inválida')

    elif computador == 1:
        if jogador == 1:
            return ('Empate')
        elif jogador == 2:
            return ('\033[0::36mJogador VENCE\033[0::36m')
        else:
            return ('Jogada Inválida')

    elif computador == 2:
        if jogador == 0:
            return ('\033[0::36mJogador VENCE\033[0::36m')
        elif jogador == 1:
            return ('\033[0::31mjogador PERDEU\033[0::31m')
        elif jogador == 2:
            return ('Empate')

        else:
            return ('Jogada Inválida')


def linha(a):
    return '-='*15

def linha2(a):
    return '~='*15



print('''Escolha:
\033[0::33m[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2] TESOURA\033[0::33m''')
jogador = int(input('Digite sua escolha: '))
computador = randint(0, 2)



print('\033[0::35mJO\033[0::35m')
sleep(1)
print('   \033[0::35mKEN\033[0::35m')
sleep(1)
print('       \033[0::35mPO!!!\033[0::35m')
sleep(0.5)
print(f'O computador jogou {itens[computador]}')
print(f'jogador jogou {itens[jogador]}')
