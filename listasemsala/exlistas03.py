# Crie um algoritmo que receba valores aleatórios (de qualquer tipo), e ao final:
# A lista em ordem inversa ao que foi lançado
# quantos dados são de cada tipo: int, str, float, bool
laco = 'S'
lista = [] # int, str, float, bool
lista2 = []
int = 0
str = 0
float = 0
bool = 0

while True != "S":
    lista = input('Digite o que quiser: ')
    if lista == "S":
        break
for i in range(len(lista)):
    try:
        lista[i] = int(lista[i])
        int += 1
    except:
        try:
            lista[i] = float(lista[i])
            float += 1
        except:
            try:
                if lista == 'True' or lista == 'False':
                    lista = bool(lista(i))
                    bool += 1
                else:
                    str +=1
            except:
                print('vai dar certo')



# print(lista)
print(int)
print(str)
print(float)
print(bool)