import pyautogui
from time import sleep


# while True:
#     print(pyautogui.position())
#     sleep(2)

'''conta a posição dos pixels da tela '''
# pyautogui.moveto(100, 100)


'''movie rel ponto 0 é a posição do mause, primeiro valor é o x segundo é o y 
terceiro é o tempo que ele vai levar pra mover o mause'''
# pyautogui.moveRel(-100, 100, 2)

'''click com o esquerdo(sempre será o click padrão'''

# pyautogui.click()
# '''esquerda'''
# pyautogui.leftClick()
# '''direito'''
# pyautogui.rightClick()
# '''duplo click'''
# pyautogui.doubleClick()
# '''triplo click'''
# pyautogui.tripleClick()

'''hotkey você pode abrir atalhos por comando'''
# pyautogui.hotkey('ctrl', 'shift', 'esc')
# pyautogui.hotkey('win', 'r')
'''key dow e key up você pode colocar temporizador'''

'''para pressionar uma tecla e soltar, diferente do hotkey que preciona e segura'''
# pyautogui.press('win')
# pyautogui.write('calculadora', interval= 0.5)
# pyautogui.press('Enter')

# with pyautogui.hold('win'):
#     pyautogui.press(['left', 'left', 'left'])

'''pra segurar com o botão direito enquanto move o mause'''

# pyautogui.dragTo(400, 300, button="left")
#
# pyautogui.hotkey('alt', 'tab')
# sleep(3)
# pyautogui.dragRel(220, 220, duration=2)
#
# pyautogui.hotkey('alt', 'tab')
# sleep(3)
# pyautogui.moveTo(162, 219)
# pyautogui.dragTo(977, 273, duration=2)

# with pyautogui.hold('alt'):
#     pyautogui.press('tab', presses=2, interval=1)

# pyautogui.alert(text="Cauan", title="alerta", button='OK')

# aaa = pyautogui.prompt(text="Adilson", title="alerta", default="")
# print('aaa')

# pyautogui.confirm(text="caun", title='alerta', buttons="OK")

# pyautogui.password(text="cauan", title="Alerta", default="", mask="*")

# x, y = pyautogui.locateOnScreen('captura7.PNG')
# pyautogui.click('Capturar.PNG')
# print(x)
