'''Uma escola está precisando de um aplicativo para calcular a
média geral dos alunos, crie uma janela capaz de receber a nota
das disciplinas de matemática, leitura, música e ciências, calcule a
média geral e ao final diga se o aluno reprovou ou passou de ano.
    Bônus: Insira imagens para caso de aprovação e reprovação.
'''

import PySimpleGUI as sg
sg.theme("SystemDefault1")

layout = [
    [sg.Text('Digite seu Nome'), sg.Input()],
    [sg.Text('Digite sua Turma'), sg.Input()],
    [sg.Text('Matemática'), sg.Spin(list(range(0, 11)),key='n1')],
    [sg.Text('Leitura'), sg.Spin(list(range(0, 11)),key='n2')],
    [sg.Text('Música'), sg.Spin(list(range(0, 11)),key='n3')],
    [sg.Text('Ciência'), sg.Spin(list(range(0, 11)),key='n4')],
    [sg.Button('Calcular')],
    [sg.Text('Média'), sg.Text(key='soma')]

  ]


janela = sg.Window('exercício 01', layout)
while True:
    eventos, valores = janela.read()
    if eventos == 'Calcular':
        janela['soma'].Update((valores['n1'] + valores['n2'] +valores['n3'] +valores['n4'])/4)

