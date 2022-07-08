'''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
Possua uma classe chamada bomba_Combustível, com no mínimo esses atributos:
tipo_Combustivel.
valor_Litro
quantidade_Combustivel
Possua no mínimo esses métodos:
abastecer_Por_Valor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecer_Por_Litro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterar_Valor( ) – altera o valor do litro do combustível.
alterar_Combustivel( ) – altera o tipo do combustível.
alterar_Quantidade_Combustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba

'''

class bomba_combustivel:
    tabela_combustivel = ['Álcool', 'Gasolina', 'Gasolina Aditivada', 'Diesel']
    tabela_valores = [5.80, 6.09, 6.19, 7.15]


    def __init__(self, tipo_Combustivel, quantidade_Combustivel):
        self.tipo_Combustivel = tipo_Combustivel
        self.quantidade_Combustivel = quantidade_Combustivel
        self.valor_Litro = self.tabela_valores[self.tabela_combustivel.index(tipo_Combustivel)]


    def alterar_Combustivel(self, novo_tipo):
        if novo_tipo in self.tipo_Combustivel:
            self.tipo_Combustivel = novo_tipo
            self.valor_Litro = self.tabela_valores[self.tabela_combustivel.index(novo_tipo)]



    def abastecer_Por_Valor(self, valor):
        litro = valor / self.valor_Litro
        print(f'Abastecendo {litro} litros de combustivel')
        self.quantidade_Combustivel -= litro


    def abastecer_Por_Litro(self, litros):
        self.quantidade_Combustivel -= litros
        print(f'Valor do abastecimento será {self.valor_Litro * litros}')


b1 = bomba_combustivel('Gasolina' , 100)
print(b1.tipo_Combustivel)
print(b1.valor_Litro)
print(b1.abastecer_Por_Valor(100))
print(b1.quantidade_Combustivel)
print(b1.abastecer_Por_Litro(20))
print(b1.quantidade_Combustivel)
