prod = []
valor = []
quant = int(input('Quantos produtos você deseja cadastrar? '))
for i in range(0, (quant)):
    n = input('produto: ')
    p = input('valor: ')
    prod.append(n)
    valor.append(p)
for j in range(0, quant):
    print(f'Produto: {prod[j]} - Preço: R${valor[j]}')