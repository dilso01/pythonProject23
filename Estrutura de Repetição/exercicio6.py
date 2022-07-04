valor = float(input('Digite o Valor do produto: '))
taxa_juros = float(input('Digite a Taxa de Juros: '))/100
num_parcelas = int(input('Digite o Número de Parcelas: '))
print(50*'=')
print('Escolha a Forma de financiamento')
print(50*'=')
modelo = int(input('digite - 1 para PRICE ou 2 para SAC: '))
amortizacao = valor / num_parcelas
parcela1 = (1 + taxa_juros)**num_parcelas * taxa_juros
parcela2 = (1 + taxa_juros)**num_parcelas - 1
parcela = valor * (parcela1 / parcela2)
if modelo == 1:
    for i in range(num_parcelas):
        juros1 = taxa_juros * valor
        amortizacao = parcela - juros1
        saldo_devedor = valor - amortizacao
        valor -= amortizacao
        print(' Nº parcelas   valora da parcela   amortização    juros    saldo devedor')
        print(f'(  {i+1}           R${parcela:.2f}             R${amortizacao:.2f}          R${juros1:.2f}   R${saldo_devedor:.2f}')
else:
    for j in range(num_parcelas):
        juros = taxa_juros * valor
        valor_parcela = amortizacao + juros
        valor -= amortizacao
        print(' Nº parcelas   valora da parcela   amortização    juros    saldo devedor')
        print(f"      {j+1}       {valor_parcela:.2f}              {amortizacao:.2f}        {juros:.2f}   {valor:.2f}")