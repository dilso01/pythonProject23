# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre conforme abaixo: A situação deve ser gerada a partir de uma função def
#
# Aluno - Jonas Reiter
# Nota - 7.5
# Situação - APROVADO

def media(a, b):
    media2 = (a + b) / 2
    return media2


def situacao(a):
    if a >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'



dic = {'nome' : input('digite o nome: '),
      'nota': float(input('Digite a nota: ')),
      'nota2': float(input('Digite a nota: '))}

dic['media'] = media(dic['nota'], dic['nota2'])
dic['status'] = situacao(dic['media'])

print(dic)


