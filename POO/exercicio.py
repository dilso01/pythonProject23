'''
# Criar uma classe para uma lata de coca-cola.
# A classe deve ter todos os atributos dimensionais,
# e suas características de material.
# As funcionalidades(métodos) da garrafa sao, abrir,
# beber, esvaziar, amassar, retirar lacre, e descartar
'''

class Lata:

    def __init__(self, altura, diametro, volume, material, rotulo):
        self.altura = altura
        self.diametro = diametro
        self.volume = volume
        self.material = material
        self.rotulo = rotulo


    def __repr__(self):
        return repr(f'{self.altura} - {self.diametro} - {self.volume} - {self.material} - {self.rotulo}')


    def abri(self):
        print('ploctzzzz')


    def beber(self):
        print('gluglugluglu')


    def esvaziar(self):
        print('lata vazia')


    def amassar(self):
        print('amassado')


    def retirar_lacre(self):
        print('Lacre retirado')


    def descartar(self):
        print('Reciclado')