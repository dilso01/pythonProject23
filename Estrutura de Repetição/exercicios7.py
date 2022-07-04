
qt_negativos = 0
qt_positivos = 0
maximo = 0
minimo = 0
cont = 0
total = 0
while True:
    num = int(input('Digite o ´numero desejado, ou 0 para parar'))
    if num == 0:
        break
    total += num
    cont += 1
    if num < 0:
        qt_negativos += 1
    else:
        qt_positivos += 1
    if maximo <= num or cont == 1:
        maximo = num
    if minimo <= num or cont == 1:
        minimo = num
print(f'Total lançado: {total}')
print(f'Quantidade de lançamento: {cont}')
print(f'Média: {total/cont}')
print(f'Positivos: {qt_positivos}')
print(f'Negativos: {qt_negativos}')
print(f'Percentual de Positivos: {qt_positivos*100/cont}')
print(f'percentual de Negativos: {qt_negativos/cont:.2%}')
print(f'Máximo: {maximo}')
print(f'Minimo: {minimo}')