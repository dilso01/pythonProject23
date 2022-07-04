anos_par = 0
anos_imp = 0
anos_bis = 0
qt_futuro = 0
qt_passado = 0

while True:
    ano = int(input('Digite um ano: ou 0 para parar'))


    if ano < 2020:
        qt_passado += 1
    else:
        qt_futuro += 1
    if ano %2 == 0:
        anos_par += 1
    else:
        anos_imp += 1
    #if ano % 400 == 0:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        anos_bis += 1
        print(f'Ano Bissexto {ano}')
    if ano == 0:
        break
print(f'Total de anos Passados: {qt_passado}')
print(f'Total de anos Futuro: {qt_futuro}')
print(f'Total de anos Bissexto: {anos_bis}')
print(f'Total de anos Ímpares: {anos_imp}')
print(f'Total de anos Pares: {anos_par}')
