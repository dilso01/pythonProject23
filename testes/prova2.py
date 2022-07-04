# Crie um programa que solicite o nome, e informe que nomes com mais de 6 caracteres são grandes,
# nomes com mais de 8 caracteres são muito grandes, Nomes com 6 ou menos caracteres são pequenos

nome = input('Digite seu nome: ')
if len(nome) <= 6:
    print('Nome pequeno')
elif len(nome)> 6 and len(nome) < 8:
    print('Nome grande')
else:
    print('Nome muito grande')