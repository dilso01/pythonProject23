from bs4 import BeautifulSoup
import requests
from operator import itemgetter

produtos = []
valores = []
geral = []

# for i in range(3):
alvo = f'https://www.malwee.com.br/collections/liquida-malwee?O=OrderByTopSaleDESC&gclid=EAIaIQobChMIkpL1wNL7-AIVhvbjBx0l0gOaEAAYASAAEgJ9SfD_BwE'
resposta = requests.get(alvo)
html = BeautifulSoup(resposta.text, 'html.parser')

for produto in html.select('.bSuzyS , .iDIZSS'):
    produtos.append(produto.text.replace("  ", '').replace('\n',''))

for valor in html.select('ins'):
    valores.append(float(valor.text.replace('.', '').replace(',', '.').replace('R$', '')))

for i in range(len(produtos)):
    novo_registro = {'Produto': produtos[i], 'Valor':valores[i]}
    geral.append(novo_registro)

lista_final = sorted(geral, key=itemgetter('Valor'), reverse=True)

for i in lista_final:
    print(i)
# 