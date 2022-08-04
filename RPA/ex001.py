from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


navegador = webdriver.Firefox()
sleep(2)
navegador.get('https://externo.proway.com.br/login-aluno')
navegador.find_element('id', 'formLoginSubscriber_username').send_keys('dilso01@icloud.com'+Keys.TAB+'26091983'+Keys.TAB+Keys.ENTER)
sleep(2)
navegador.maximize_window()
navegador.find_element('xpath', '/html/body/div[1]/section/section/main/div/div/div/ul/li[1]/ul/li/button/span[2]').click()
