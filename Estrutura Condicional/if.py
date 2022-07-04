nome = input("digite seu nome: ").upper()
n1 = int(input("digite a nota 1: "))
n2 = int(input("digite a nota 2: "))
n3 = int(input("digite a nota 3: "))
n4 = int(input("digite a nota 4: "))

media = (n1 + n2 + n3 + n4) / 4

if media >= 7:
    print(f"{nome}, Você foi aprovado")
elif media >= 5:
    print (f"{nome}, Você ficou em exame")
else:
    print(f"{nome}, estude mais seu bagunceiro")
