# Crie um código solicite login e senha para dar acesso ao sistema.
# Já deverá estar previamente cadastrado no código as 3 primeiras letras
# do seu nome como usuário e sua data de nascimento sem separadores como senha.

log = str('adi')
sen = int(26091983)
login = print(input('Digite seu login: '))
senha = print(int(input('Digite sua senha: ')))

if log != login and sen != senha:
    print('Sua entrada foi liberada')

else:
   print('Login e senha não confere, tente novamente')
