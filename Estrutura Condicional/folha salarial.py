
# Escreva um programa que receba:
# Nome: jonas reiter
# Cargo: (1) Professor (2) Coordenador (3) Zelador
# Salário: 4.0000,00

# Calcular o  novo salário, que é 10% sobre o valor atual.
# Calcular o salário Líquido:

#     - Bonificação: 5% sobre o salário bruto novo
#     - IRRF:
#         salário de até R$1.999,00 estão isentos do IR;
#         faixa salarial de R$1.999,00 a R$2.967,00: alíquota de 7,5%;
#         faixa salarial de R$2.967,00 a R$3.938,00: alíquota de 15%;
#         faixa salarial de R$3.938,00 a R$4.987,00: alíquota de 22,5%;
#         acima de R$4.987,00: aliquota de 27,5%.

# Ao final, trazer:

# -------------------------------------------------------
# Colaborador: JONAS REITER < - Maiúsculo
# Cargo: PROFESSOR < - Maiúsculo
# Salário Novo: 4400.00 reais
# Bonificação: 220.00 reais
# IRRF: 990.00 reais
# Salário Líquido: 3630.00 reais
# ____________________________________________________________

nome = input('Digite o seu nome: ')
cargo = input('Digite o seu cargo: (1) Professor (2) Coordenador (3) Zelador: ')
salario = float(input('Digite o seu Salário Atual: '))
salario_novo = salario * 1.1
bonificacao = salario_novo * 0.05

if salario_novo < 1999:
    irrf = 0
elif salario_novo < 2967:
    irrf = salario_novo * 0.075
elif salario_novo < 3938:
    irrf = salario_novo * 0.15
elif salario_novo < 4987:
    irrf = salario_novo * 0.225
else:
    irrf = salario_novo * 0.275

salario_liquido = salario_novo - irrf + bonificacao

print(f'COLABORADOR: {nome.upper()}')
if cargo == '1':
    print('CARGO: PROFESSOR')
elif cargo == '2':
    print('CARGO: COORDENADOR')
else:
    print('CARGO: ZELADOR')

print(f'Salário Novo: {salario_novo:.2f}')
print(f'Bonificação: {bonificacao:.2f}')
print(f'IRRF: {irrf:.2f}')
print(f'Salário líquido: {salario_liquido:.2f}')
