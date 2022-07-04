'''criar um algoritmo que receba 4 notas e o nome do aluno,
usar os seguintes criterios;
nota entre 5 e 7 = exame
nota entre 7 e 9 aprovado
nota 10 = super aprovado
nota entre 3 e 5 volte duas casas e tente novamente
nota de 0 a 3 hoje nao Faro
'''

nome = input("digite o nome: ").upper
n1 = int(input(digite a nota 1))
n2 = int(input(digite a nota 2))
n3 = int(input(digite a nota 3))
n4 = int(input(digite a nota 4))
media = (n1 + n2 + n3 + n4) / 4

if media = 10:
    print(f"{nome}, SUPER APROVADO")
elif media >= 9:
    print(f"{nome}, você está aprovado com estrelinha ***")
elif media >= 7:
    print(f"{nome}), APROVADO")
elif media >= 5:
    print(f"{nome}, exame")
elif media >= 3:
    print(f"{nome},volte duas casas e tente novamente")
else:
    print(f"{NOME}, HOJE NÃO FARO")