class Conta:
    def __init__(self, agencia, conta, saldo=0.0):
        self.agencia = agencia
        self.conta = conta
        self.__saldo = saldo


    def depositar(self, valor):
        self.__saldo += valor
        self.__mensagem()

    def ver_saldo(self):
        print(self.__saldo)



    def __mensagem(self):
        print(f'Bom dia, seu depósito foi feito')


c1 = Conta(3365, '1234-5')
c1.ver_saldo()
c1.depositar(200)
c1.ver_saldo()





# c1.ver_saldo()

# print(c1.__saldo)
# c1.depositar(200)
# print(c1.__saldo)
#
