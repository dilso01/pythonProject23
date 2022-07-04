# # Conversão de número para Hexadecimal PYTHON
# W3SCHOOLS - FORMAT
# receber os valores de R, G e B, e ao final
# apresentar o Código Hexadecimal
# EX: R - 255
#     G - 255
#     B - 160
# RESPOSTA: #FFFFA0
# Não pode lançar valores para R, G ou B que estejam fora dos números
# 0 a 255

r = int(input('Digite o valor de RED: '))
g = int(input('Digite o valor de RED: '))
b = int(input('Digite o valor de RED: '))

if r > 255 or r < 0 or g > 255 or g < 0 or b > 255 or b < 0:
    print('Revise os números')
else:
    print(f'#{r:02X}{g:02X}{b:02X}')