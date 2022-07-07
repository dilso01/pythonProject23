'''
Classe Retangulo: Crie uma classe que modele um retângulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local.
Depois, deve-se criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessários para o local.

'''

class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura


    def mudar_valor_comprimento(self, novo_comprimento):
        self.comprimento = novo_comprimento


    def mudar_valor_largura(self, novo_largura):
        self.largura = novo_largura


    def valor_lados(self):
        print(f'Retangulo tem por medidas de comprimento {self.comprimento} e largura {self.largura}')


    def calcular_area(self):
        print(f'A área total é {self.largura * self.comprimento}')


    def calcular_perimetro(self):
        print(f'O perimêtro deste triângulo é {(self.largura + self.comprimento) * 2}')


r1 = Retangulo




#calcular a quantidade de pisos
