'''2-Faça um gráfico de pizza que aponte as áreas de um curso apontando a porcentagem de cada área:
-TI=50%
-Administração=30%
-Engenharia civil=10%
-Inglês=10%
-E colocar legendas para informar os nomes de cada área
'''

import matplotlib.pyplot as plt
import numpy as np
y = np.array([50, 30, 10, 10])
mylabels = ["TI", "ADM", "Eng.Civil", "Inglês"]
myexplode = [0, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()