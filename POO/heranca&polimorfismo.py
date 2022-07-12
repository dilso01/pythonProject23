class Veiculo:
    def __init__(self, cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo):
        self.cor = cor
        self.lugares = lugares
        self.qtd_pneus = qtd_pneus
        self.tipo_motor = tipo_motor
        self.valor = valor
        self.ano = ano
        self.marca = marca
        self.modelo = modelo


    def acelerar(self):
        print('Acelerou')


    def frear(self):
        print('Freou')


    def ligar(self):
        print('Ligou')


    def desligar(self):
        print('Desligou')


class Moto(Veiculo):
    def __init__(self, cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo, empinada=False):
        super().__init__(cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo)
        self.empinada = empinada



    def empinar(self):
        if self.empinada:
            print('Já está empinada')
        else:
            print('Impinaaaaa')
            self.empinada = True

    def desempinar(self):
        self.empinada = False



class Carro(Veiculo):
    def __init__(self, cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo, encosto_cabeca=True,
                 retrovisor_interno=True):
        super().__init__(cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo)
        self.encosto_cabeca = encosto_cabeca
        self.retrovisor_interno = retrovisor_interno



    def retrovisor(self):
        self.retrovisor_interno = False
        print('Sem Visão não tem como')


    def encosto(self):
        self.encosto_cabeca = False
        print('Sua segurança está em risco')




class Onibus(Veiculo):
    def __init__(self, cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo, qtd_portas, catraca=True):
        super().__init__(cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo)
        self.qtd_portas = qtd_portas
        self.catraca = catraca


    def portas(self, num_portas):
        self.qtd_portas = num_portas
        print(f'Seu onibus tem {self.qtd_portas} portas!')



    def sem_catraca(self):
        self.catraca = False



m1 = Moto('Azul', 2, 2, '125cc', 17000, 2022, 'Honda', 'CG-125', True)

print(m1.tipo_motor)
m1.empinar()
m1.desempinar()
m1.empinar()


v1 = Veiculo('Preto', 4, 4, '180cv', 45000, 2012, 'Chevrolet', 'Celta')

#criar uma classe herdeira carro e outra onibus.
#As 2 classes novas precisam ter 2 métodos novos e 2 atributos novos cada

