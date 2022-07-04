import requests
a = input('Digite seu CEP: ')
r = requests.get('https://cep.awesomeapi.com.br/json/'+a)
r = r.json()
if r == 200:
    print('cep valido')
else:
    print('cep oinvalido')