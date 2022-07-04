'''3- Faça um gráfico de barras apontando janeiro, fevereiro e março na linha x e na linha y apontar
quantidade de pessoas que visitaram o Hotel do JonasExProfessor com as seguintes informações:
-A cor do título tem que ser azul;
-A cor das barras tem que ser vermelhas
-Os números de visitantes foram:(3, 8, 1) ;

'''

import matplotlib.pyplot as plt
import numpy as np
x = np.array(['Janeiro', 'Fevereiro', 'Março'])
y = np.array([3, 8, 1])
plt.bar(x,y, color="red")
plt.title('JonasExProfessor', color='b')
plt.ylabel('Pessoas', color='y')
plt.xlabel('Meses', color='y')
plt.show()
