'''
Classe TV: Faça um programa que simule um televisor criando-o como um
objeto. O usuário deve ser capaz de informar o número do canal e aumentar
ou diminuir o volume. Certifique-se de que o número do canal e o nível do
volume permanecem dentro de faixas válidas

'''


class Tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume
        self.ligada = True


    def mudar_canal(self, novo_canal):
        if self.canal != novo_canal:
            self.canal = novo_canal
            print(f'Você trocou de canal para {novo_canal}')
        else:
            print('Você ja está assitindo este canal')


    def mudar_volume(self, novo_volume):
        if self.volume != novo_volume:
            self.volume = novo_volume
            print(f'Seu volume está foi aumentado para {novo_volume}')
        else:
            print(f'Você ja está nesse volume {novo_volume}')


    def desligar(self):
        self.ligada = False
        print('Desligando...')


    def qual_volume(self):
        print(f'Seu volume está em {self.volume}')


    def qual_canal(self):
        print(f'Você esta assistindo o canal {self.canal}')

t1 = Tv(35, 44)
t1.qual_volume()
t1.mudar_volume(55)
t1.qual_canal()
t1.mudar_canal(555)
t1.desligar()