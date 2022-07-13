from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, especie, habitat):
        self.nome = nome
        self.especie = especie
        self.habitat = habitat

    @abstractmethod
    def pedir_comida(self):
        return True

    def comer(self):
        print(f'{self.nome} Comeu')

    @staticmethod
    def nascer():
        print('Nasceu')

    @classmethod #quando eu quero chamar o metodo pra classe não para a instancia
    def morrer(cls):
        print('Morreu')


class Felino(Animal):
    def __init__(self, nome, especie, habitat, garras, orelhas):
        super().__init__(nome, especie, habitat)
        self.orelhas = orelhas
        self.garras = garras

    def pedir_comida(self):
        print('Miaauuu')

gato = Felino('Milka', 'Gato', 'Mato', True, 2)
gato.pedir_comida()
Animal.morrer()