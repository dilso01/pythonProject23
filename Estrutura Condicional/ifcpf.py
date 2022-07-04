# 0	Rio Grande do Sul
# 1	Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins
# 2	Amazonas, Pará, Roraima, Amapá, Acre e Rondônia
# 3	Ceará, Maranhão e Piauí
# 4	Paraíba, Pernambuco, Alagoas e Rio Grande do Norte
# 5	Bahia e Sergipe
# 6	Minas Gerais
# 7	Rio de Janeiro e Espírito Santo
# 8	São Paulo
# 9	Paraná e Santa Catarina

cpf = input('Digite o seu CPF: ')
estado = cpf[10]
if estado == '0':
    print('Rio Grande do Sul')
elif estado == '1':
    print('Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins')
elif estado == '2':
    print('Amazonas, Pará, Roraima, Amapá, Acre e Rondônia')
elif estado == '3':
    print('Ceará, Maranhão e Piauí')
elif estado == '4':
    print('Paraíba, Pernambuco, Alagoas e Rio Grande do Norte')
elif estado == '5':
    print('Bahia e Sergipe')
elif estado == '6':
    print('Minas Gerais')
elif estado == '7':
    print('Rio de Janeiro e Espírito Santo')
elif  estado == '8':
    ('São Paulo')
elif estado == '9':
    print('Paraná e Santa Catarina')

print(estado)