import Pillow
from PIL import Image
from time import sleep
linha = '~='*15

'''fonte. https://www.anamariabrogui.com.br/receita/pastelao-de-liquidificador-321270'''


ingredients = ["2 cups of wheat", "1 cup of milk", "1/2 cup of oil", "3 eggs", "1/2 cup grated cheese",
"1 spoon of baking powder", ]

#Tradução
ingredientes = ["2 xícaras de farinha de trigo", "1 xícara de leite", "1/2 xícara de oleo", "3 ovos", "1/2 xícara de queijo ralado",
"1 colher de fermento em pó"]



filling = ["400 g of mozzarella cheese", "3 oil collections", "1 kg of minced meat", "1 large tomato",
 "1 medium onion", "1 Salt", "chives and parsley to taste"]

#Tradução
recheio = ["400 g de queijo mussarela", "3 colheres de oleo", "1 kg de carne moída", "1 tomate grande", "1 cebola média",
"Sal", "cebolinha e salsa a gosto"]


preparation_mode = ["1. Put the oil in a pan along with the chopped onion, the tomato and let it sauté"
"2. Then place the meat and let it sauté", "3. Add the other ingredients and let it settle", "4. After preparing the filling, set aside"]

modo_preparacao = ["Bater no liquidificador todos os ingredientes e reservar",
"6 Colocar em uma forma média, uma camada da massa e cobrir com metade do queijo, em cima colocar metade do recheio",
"7 Em seguida, colocar a outra metade da massa e cobrir com o restante do queijo e do recheio",
"8 Levar ao forno por aproximadamente 45 minutos"]

pasta = [ "5 Blend all ingredients in a blender and set aside",
" 6 Put a layer of the dough in a medium shape and cover with half the cheese, on top put half the stuffing",
" 7 Then place the other half of the dough and cover with the rest of the cheese and the filling",
" 8 Bake in the oven for approximately 45 minutes"]

massa = ["Bater no liquidificador todos os ingredientes e reservar",
"6. Colocar em uma forma média, uma camada da massa e cobrir com metade do queijo, em cima colocar metade do recheio",
"7. Em seguida, colocar a outra metade da massa e cobrir com o restante do queijo e do recheio",
"8. Levar ao forno por aproximadamente 45 minutos"]


print(linha)
print('Ingredients'.center(30))
print(linha)
for i in ingredients:
    print(i)
    sleep(0.5)
print()
print(linha)
print('Tradução'.center(30))
print(linha)
print()
for i in ingredientes:
    print(i)
    sleep(0.5)
print()
print(linha)
print('Filling'.center(30))
print(linha)
print()
for i in filling:
    print(i)
    sleep(0.5)
print()
print(linha)
print('Tradução'.center(30))
print(linha)
for i in recheio:
    print(i)
    sleep(0.5)
print()
print(linha)
print('Preparation Mode'.center(30))
print(linha)
print()
for i in preparation_mode:
    print(i)
    sleep(0.5)
print()
print(linha)
print('Tradução'.center(30))
print(linha)
print()
for i in modo_preparacao:
    print(i)
    sleep(0.5)
print()
print(linha)
print('Pasta'.center(30))
print(linha)
print()
for i in pasta:
    print(i)
    sleep(0.5)
print()
print(linha)
print('Tradução'.center(30))
print(linha)
print()
for i in massa:
    print(i)
    sleep(0.5)