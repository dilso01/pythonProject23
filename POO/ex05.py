'''
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho
(estômago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa
ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo
menos 3 alimentos diferentes e verificando o conteúdo do estômago a cada refeição.
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

'''
estomago =[]
class Macaco:
    def __init__(self, nome, bucho=True):
        self.nome = nome
        self.bucho = bucho



    def comer(self, alimento):
       print(f'Você comeu {alimento}')
       estomago.append(alimento)


    def ver_estomago(self):
        print(self.bucho)
        print(estomago)



    def digerir(self):
        estomago.clear()
        self.bucho = False
        print('Estomago vazio')




m1 = Macaco('Pedro')
m2 = Macaco('Joao')
m1.comer('maça')
m2.comer('uva')
m1.ver_estomago()
m2.ver_estomago()
m1.comer('banana')
m2.comer(m1)
m1.comer('morango')
m1.ver_estomago()
m1.digerir()
m1.ver_estomago()
