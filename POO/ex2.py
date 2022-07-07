'''
Classe Quadrado: Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

'''

class Quadrado:
    def __init__(self, tamanho):
        self.tamanho = tamanho


    def mudar_valor(self, novo_valor):
        self.tamanho = novo_valor
        print(f'Novo Valor do Quadrado é {novo_valor}')



    def retornar(self):
        print(f'O valor de cada lado é {self.tamanho}')


    def calcular_area(self):
        print(f'A área do quadrado é {self.tamanho**2}')


q1 = Quadrado(7)
q1.retornar()
q1.calcular_area()
q1.mudar_valor(5)
q1.calcular_area()



