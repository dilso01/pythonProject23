'''Classe Bola: Crie uma classe que modele uma bola:
Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor'''


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material


    def trocar_cor(self, nova_cor):
        if self.cor != nova_cor:
            self.cor = nova_cor
            print(f'Bola recebou uma nova cor {nova_cor}')
        else:
            print('Bola já era dessa cor')

    def mostra_cor(self):
        print(self.cor)


b1 = Bola('Branca', 78, 'Couro')
b1.trocar_cor('azul')