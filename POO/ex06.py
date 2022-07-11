'''
Classe Bichinho Virtual:Crie uma classe que modele um Tamagotchi (Bichinho Eletrônico):
Atributos: Nome, Fome, Saúde e Idade.
Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
Obs: Existe mais uma informação que devemos levar em consideração,
o Humor do nosso tamagotchi, este humor é uma combinação
entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos
criar um atributo para armazenar esta informação por que ela pode ser calculada a
qualquer momento.

'''

class Tamagotchi:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.fome = True
        self.saude = True
        self.brincar = False
        self.comer = False



    def trocar_nome(self, novo_nome):
        if self.nome != novo_nome:
            self.nome = novo_nome
            print(f'Seu Tamagotchi recebeu um novo nome {novo_nome}')


    def trocar_idade(self, novo_idade):
        if self.idade != novo_idade:
            self.idade = novo_idade
            print(f'Seu Tamagotchi recebeu um nova idade {novo_idade}')



    def alterar_saude(self):
        self.saude = False


    def qual_nome(self):
        print(f'Meu nome é {self.nome}')


    def qual_idade(self):
        print(f'A minha idade é {self.idade}')



    def esta_fome(self):
        if self.fome == False:
            print('Não estou com fome')
        else:
            print('Sim estou com fome')



    def alimentar(self):
        self.fome = False




    def sua_saude(self):
        if self.saude == False:
            print('Não estou muito bem')
        else:
            print('Sim estou muito bem')



t1 = Tamagotchi('xuxu', 3)
t1.trocar_nome('tuca')
t1.qual_idade()
t1.esta_fome()
t1.alimentar()
t1.esta_fome()
t1.sua_saude()
t1.trocar_idade(5)