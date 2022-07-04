# Criar um programa em 2 arquivos, 1 para as funções, e outro para o código:
# O programa deve ter as seguintes funcionalidades:
# Receber as medidas de um triângulo:
# verificar se é um triângulo verdadeiro
# verificar qual o tipo de triângulo

import funcoesEx as f

l1 = int(input('Solicite a primeura medida: '))
l2 = int(input('solicite a segunda medida: '))
l3 = int(input('solicite a terceira medida: '))

print(f.triangulo(l1,l2,l3))



