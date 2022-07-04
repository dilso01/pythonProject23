'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.

Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário. '''
ano = 2022
dic = {'nome' : input('digite o nome: '),
      'Ano Nasc': int(input('Digite o ano Nascimento: ')),
      'Carteira Trabalho': 2321}
Ctps = int(input('Digite o número Carteira de trabalho: '))
if Ctps == 0:
    dic['Carteira Trabalho'] = ['Desempregado']
else:
    dic['Carteira Trabalho'] = Ctps
    dic['Ano Contratação'] = int(input('Digite o ano da contratação: '))
    dic['idade'] = ano - dic['Ano Nasc']
    dic['salario'] = float(input('Digite o salario: '))
    # dic['aposentadoria'] = dic['Ano Contratação'] - ano



print(dic)