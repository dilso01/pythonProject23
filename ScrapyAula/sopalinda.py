from bs4 import BeautifulSoup
import requests
from operator import itemgetter

alvo = f'https://www.bistek.com.br/bebidas/vinhos-e-espumantes.html'
resposta = requests.get(alvo)
html = BeautifulSoup(resposta.text, 'html.parser')
produtos = []
valores = []
geral = []
for produto in html.select('.product-item-link'):
    produtos.append(produto.text.replace("  ", '').replace('\n', ''))

for valor in html.select('.price-wrapper .price'):
    valores.append(float(valor.text.replace('.', '').replace(',', '.').replace('R$ ','')))

for i in range(len(produtos)):
    #print(f'{produtos[i]} + {valores[i]}')
    novo_registro = {'Produto': produtos[i], 'Valor': valores}
    geral.append((novo_registro))

lista_final = sorted(geral, key=itemgetter('Valor'), reverse=True)
print()