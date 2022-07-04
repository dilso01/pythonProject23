# Adapte o programa da questão anterior,  para que ele não permita lançar notas que não estão entre 0,0 e 10,0


# Adapte novamente o programa anterior, solicitando antes das notas a frequência do aluno e classificando entre aprovado
# (frequência maior ou igual a 75% e média maior ou igual a 7,0)





freq = float(input('Digite a frequencia do aluno: '))
nota = 0
for i in range(0, 3):
    nota1 = float(input('Digite a nota: '))
    nota += nota1
if nota >= 7.0 or freq >= 75:
    print('Você foi aprovado')
else:
    print('Reprovado')

# print(f'A média da sua nota é {nota/3:.2f}')