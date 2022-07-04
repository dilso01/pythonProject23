import PySimpleGUI as sg
sg.theme("SystemDefault1")

layout = [
    [sg.Frame(],
    [sg.Text('Digite seu Nome'), sg.Input()],
    [sg.Text('Idade'), sg.Input()],
    [sg.Button('OK')]]

janela = sg.Window('Aula', layout)
janela.read()


