# Faça uma função que retorne o reverso de um número inteiro informado.
# Por exemplo: 127 -> 721.

def invertido(numero):
    numero = str(numero)
    return numero[::-1]

valor = 456
print(invertido(valor))

