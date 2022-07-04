from operator import itemgetter

times = {'Palmeiras': 18,
         'Flamengo': 12,
         'Coritiba': 22}

print(times)
#para ordenar
timesnovo = sorted(times.items(), key=itemgetter(1), reverse=True)


#para imprimir um item específico

print(timesnovo)
print(timesnovo[1][1])

#para printar a lista com o enumeraate
for i, time in enumerate(timesnovo):
    print(f'{i + 1} - {time[0]} - {time[1]}')

