import PySimpleGUI as sg
# sg.theme_previewer()

# theme_name_list=sg.theme_list()

# print utilizando o biblioteca
# sg.popup('Olá Mundo!!')

# sg.popup_ok_cancel('Olá mundo')

# sg.popup_notify('Enviado')

# layout = [
#     sg.Text('Olá, Mundo')]

# layout = [
#     [sg.Text('Olá Mundo')],
#     [sg.Button('OK')]
# ]
#
# janela = sg.Window('Título', layout)
# janela.read()

# sg.popup('Adilson')
#
# layout = [
# #     [sg.Text('Olá Mundo')],
# # [sg.input()],
# # [sg.Multiline()],
# # [sg.Combo(['Paulo', 'Rodrigo'])],
# # [sg.Checkbox('Deficiente')],
# # [sg.Radio('Sim', 'opc'), sg.Radio('Não', 'opc'), sg.Radio('Talvez', 'opc')],
# # [sg.Spin(list((range(1, 100))))],
# # [sg.Slider((1, 100))],
# # [sg.Button('OK')],
# # [sg.Image(r'C:\Users\guest01\Documents\Nova pasta')],
# [sg.Frame('Janela Frame', [
#           [sg.Text('Frase')]]
# # ]

# janela = sg.Window('Aula', layout)
# janela.read()

# SALVAR VALORES E EVENTOS
# layout = [
#     [sg.Input(Key='Nome')],
#     [sg.Button('Salvar')]
# ]
# janela = sg.Window('Aula', layout)
# eventos, valores = janela.read()
# print(eventos)
# print(valores)



#  size tamanho e altura, font para tamanho da letra, justification = 'r' 'l' 'c'


CÓDIGO

import PySimpleGUI as sg

# print(sg.theme_list())


# print('Olá, Mundo')



# sg.popup('Olá, Mundo!')


# sg.popup_ok_cancel('Olá, Mundo')


# sg.popup_notify('Enviado!')


# Composição base de uma janela
# layout | janela | ler janela


# layout = [
#      [sg.Text('Ola, Mundo!')]
#  ]

#
# layout = [
#     [sg.Text('Olá, Mundo!')],   #Atenção para a vírgula
#     [sg.Button('OK')]
# ]


# janela = sg.Window()


# janela = sg.Window('Título', layout)


# janela = sg.Window('Aula', layout)
#
#
# janela.read()


# Criar janela com seu nome e um botão


# layout = [
#     [sg.Text('Olá, Mundo!')],
#     [sg.Input()],
#     [sg.Multiline()],
#     [sg.Combo(['Paulo', 'Rodrigo'])],
#     [sg.Checkbox('Deficiente?')],
#     [sg.Radio('sim', 'a'), sg. Radio('nao', 'a'), sg. Radio('talvez', 'a')],
#     [sg.Spin(list(range(1, 100)))],
#     [sg.Slider((1, 100))],
#     [sg.Button('OK')],
#     # [sg.Image(r'C:\Users\Usuario\Pictures\Saved Pictures\calculator-1.png')],
#     [sg.Text('OLA MUNDO')],
#     [sg.Frame('Janela Frame', [
#         [sg.Text('Frase')],
#         [sg.Button('OK')]
#     ])],
# ]
# janela = sg.Window('Aula', layout)
# janela.read()


# SALVAR VALORES E EVENTOS
# layout = [
#     [sg.Input(key='Nome')],
#     [sg.Button('Salvar')]
# ]
# janela = sg.Window('Aula', layout)
# eventos, valores = janela.read()
# print(eventos)
# print(valores)
# if eventos == 'Salvar':
#     print('Nome salvo')
#     print(valores['Nome'])


# WHILE TRUE
# layout = [
#     [sg.Input(key='nome')],
#     [sg.Slider((1, 100))],
#     [sg.Button('OK')]
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     print(eventos)
#     print(valores)
#     if eventos == 'Salvar':
#         print('Nome salvo')
#         print(valores['nome'])
#     elif eventos == sg.WINDOW_CLOSED:
#         break


# ATUALIZAR VALORES
# layout = [
#     [sg.Text('OLA MUNDO', key='txt')],
#     [sg.Input(key='nome')],
#     [sg.Button('Salvar', key='btn')],
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     print(eventos)
#     print(valores)
#     print(type(janela))
#     if eventos == 'btn':
#         janela['nome'].Update('PAULO')
#         janela['txt'].Update('PAULO')
#     elif eventos == sg.WINDOW_CLOSED:
#         break


# ATRIBUTOS
# layout = [
#     # [sg.Input(key='nome', default_text='Digite aqui', background_color='Cyan')],
#     # [sg.Button('Salvar')],
#     # [sg.Slider((1.0, 11.0), orientation='h', size=(30, 20), key='slider')],
#     [sg.Text('OLA MUNDO', size=(30, 1), font=30, justification='r')],
#     [sg.Slider((1, 100), enable_events=False, key='slider', orientation='h')],
#     [sg.Button('Salvar')]
#
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     print(eventos)
#     print(valores)
#     if eventos == 'Salvar':
#         janela['slider'].Update(range=(1, 10))


# FECHAR JANELA
# layout = [
#     [sg.Input(key='nome')],
#     [sg.Button('Salvar')]
#
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     print(eventos)
#     print(valores)
#     if eventos == 'Salvar':
#         janela.close()    #Janela não pode ser mais reaberta
#         break



# # REABRIR JANELA
# txtBotao = 'Salvar'
# layout = [
#     [sg.Input(key='nome')],
#     [sg.Button(txtBotao)],
#     [sg.Combo(sg.theme_list(), key='combolista')]
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     if eventos == 'Salvar':
#         # print(sg.theme_list())
#         sg.theme(valores['combolista'])
#         txtBotao = 'ola'
#         janela.close()
#         layout = [
#             [sg.Input(key='nome')],
#             [sg.Button(txtBotao)],
#             [sg.Combo(sg.theme_list())]
#         ]
#         janela = sg.Window('Aula', layout)
#         eventos, valores = janela.read()
#         break