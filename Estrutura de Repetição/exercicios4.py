laço = 'S'
#input('Deseja ver uma tabuada? [S/N]').strip().upper()[]
while laço == 'S':
    input('Deseja ver uma tabuada? [S/N]').strip().upper()
    if laço != 'S':
        break
    tab = int(input('Tabuada de? '))
    for i in range(0, 11):
        print(f'{tab:^4} X {i:^4} = {tab * i:^4}')
