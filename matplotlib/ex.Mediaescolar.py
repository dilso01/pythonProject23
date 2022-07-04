import matplotlib.pyplot as plt
import numpy as np
print(30*"=")
print("GRÁFICOS DE MÉDIAS DO SEMESTRE")
print(30*"=")
nomes = []
notas = []
vezes = int(input("Digite quantas médias serão lançadas: "))
for i in range(vezes):
    nomes.append(input("Digite o nome do aluno(a): "))
    notas.append(float(input("Digite a média: ")))
if len(notas) == len(nomes):
    x = np.arange(len(notas))
    colors=[]
    for i in range(len(notas)):
        if notas[i]>=7:
            colors.insert(i, "green")
        else:
            colors.insert(i, "red")
    fig, ax = plt.subplots()
    ax.bar(x, notas, alpha=0.5, color=colors)
    plt.axhline(y = 7, color = 'k', linestyle = '-')
    plt.suptitle("Média dos alunos")
    plt.title("Média baseada nas notas do decorrente semestre")
    plt.xticks(x, nomes)
    plt.show()
else:
    print("Verifique os seus dados")
