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


    def calcular_perimetro1(self):
        print(f'O perimêtro deste Retângulo é {(self.largura + self.comprimento) * 2}')


    def calcular_perimetro(self):
         return (self.largura + self.comprimento) * 2


    def calcular_q_pisos(self):
        print()


sala = Retangulo(500, 300)
piso = Retangulo(40, 25)

sala.calcular_area()
piso.calcular_area()
# qp = (sala / piso)
print(f'Quantidade de rodapés necessario {sala.calcular_perimetro()}')
# print(f'Quantidade de pisos necessário é {qp}')
sala.calcular_perimetro1()
piso.valor_lados()





#calcular a quantidade de pisos
