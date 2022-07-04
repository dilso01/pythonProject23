mulheres = []
homens = []
for i in range(1, 4):
    nome = input(f'mulher {i}: ')
    mulheres.append(nome)
print()
print(f'{mulheres}\n')

for j in range(0, 3):
    nome1 = input(f'homem {i}: ')
    homens.append(nome1)
print()
print(f'{homens}\n')

for k in range(0, 3):
    print(f'Dupla: {homens[k]} e {mulheres[k]} '.replace("[]", ''))



