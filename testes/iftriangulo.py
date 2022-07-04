#Solicitar as 3 medidas de 1 triângulo
#Após isso, verificar se as medidas realmente
#formam um triângulo, e digam, caso seja um
#triângulo possível, qual tipo de triângulo é
#Equilátero, Isóceles, Escaleno
#Critério para saber se é um triângulo
#Um dos lados nunca pode ser maior que a soma5
#dos outros 2 lados5
#Critério para saber se é um triângulo
#Um dos lados nunca pode ser maior que a soma5
#dos outros 2 lados5

#Equilátero: todos os lados são iguais
#Isóceles: 2 lados iguais e 1 diferente
#Escaleno: 3 lados diferentes'''


l1 = int(input('Solicite a primeira medida: '))
l2 = int(input('solicite a segunda medida: '))
l3 = int(input('solicite a terceira medida: '))

if l1 + l2 < l3 or l2 + l3 < l1 or l1 + l3 < l2:
    print('Não é um triangulo')
elif l1 == l2 == l3:
#and l2 == l3 == l1 and l1 == l3 == l2:
    print('Sim é um Triangulo Equilátero')
elif l1 != l2 != l3:
#and l2 != l3 != l1 and l1 != l3 != l2:
    print('Sim é um Triangulo Escaleno')
else:
    print('Sim é um Triangulo Isósceles')

