''' fazer classe mãe chamada animal, e classes filhas
ex: felinos, caninos, reptil, ovinos, peixes , aves
'''

class Animal:
    def __init__(self, patas, pele, tipo_alimento, sexo):
        self.patas = patas
        self.pele = pele
        self.tipo_alimento = tipo_alimento
        self.sexo = sexo


    def comer(self):
        print('Comendo....')


    def correr(self):
        print('Correndo...')


    def saltar(self):
        print('Saltando...')


    def dormir(self):
        print('Dormindo...')


class Felinos(Animal):
    def __init__(self, patas, pele, tipo_alimento, sexo, cacar=True, garras=True):
        super().__init__(patas, pele, tipo_alimento, sexo)
        self.cacar = cacar
        self.garras = garras


    def cacando(self):
        if self.cacar == True:
            print('Silêncio, estou atrás de uma presa.')
        else:
            print('Hora da diversão, não estou com fome agora')


    def ini_cacar(self):
        self.cacar = True
        print('Vou caçar, estou com fome')


    def parar_cacar(self):
        self.cacar = False
        print('Não vou caçar mais')


class Reptil(Animal):
    def __init__(self, patas, pele, tipo_alimento, sexo, cor, sol=False):
        super().__init__(patas, pele, tipo_alimento, sexo)
        self.cor = cor
        self.sol = sol


    def pegar_sol(self):
        self.sol = True
        print('Pegando sol pra esuqentar meu sangue')


    def trocar_pele(self):
        print('Minha pele está sendo renovada...')


class Humano(Animal):
    def __init__(self, patas, pele, tipo_alimento, sexo, estilo_roupa, pensar=True):
        super().__init__(patas, pele, tipo_alimento, sexo)
        self.estilo_roupa = estilo_roupa
        self.pensar = pensar


    def estudar(self):
        print('Estudando...')


    def falar(self):
        print('Falando...')


    def Parar_falar(self):
        print('Parou de falar.')


    def pensar(self):
        print('Pensando...')


class Peixes(Animal):
    def __init__(self, patas, pele, tipo_alimento, sexo, num_nadadeiras, cor):
        super().__init__(patas, pele, tipo_alimento, sexo)
        self.num_nadadeiras = num_nadadeiras
        self.cor = cor

    def nadar(self):
        print('Nadando...')


    def parar_nadar(self):
        print('Não está nadando')

    def ir_fundo(self):
        print('Está no fundo...')

    def ir_superficie(self):
        print('Está na superfície...')


tigre = Felinos(4, 'pelos', 'carne', 'M', )
tigre.cacando()
tigre.correr()
tigre.saltar()
tigre.comer()


