"""criar um algoritmo que receba 3 numeros,
e ao final, os apresente em ordem crescente e decrecente
"""

n1 = 367
n2 = 590
n3 = 333

if n1 > n2: # Verificar se o n1 é maior que o n2
    n1, n2 = n2, n1
if n1 > n3: # Verificar se o n1 é maior que o n3
    n1, n3 = n3, n1
if n2 > n3: # Verificar se o n2 é maior que o n3
    n2, n3 = n3, n2

print(n1, n2, n3)
print(n3, n2, n1)