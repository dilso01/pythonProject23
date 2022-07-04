'''
4-Altere o gráfico anterior colocando na horizontal, aumente a tela de exibição, aumente os tamanhos das letras,
mude as cores das legendas para ‘amarelo’ e coloque o auxílio quadriculado para ajudar na visualização do gráfico.


'''

import matplotlib.pyplot as plt
import numpy as np


x = np.array(['Janeiro', 'Fevereiro', 'Março'])
y = np.array([3, 8, 1])
plt.barh(x,y, color="red")
plt.title('JonasExProfessor', color='k')
plt.ylabel('Pessoas', color='g')
plt.xlabel('Meses', color='g')
plt.grid()

plt.show()
