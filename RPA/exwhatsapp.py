from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


navegador = webdriver.Firefox()
sleep(2)
navegador.get('https://web.whatsapp.com/')
sleep(20)
navegador.find_element('xpath', '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]').click()
navegador.find_element('xpath', '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]').send_keys('gabriel Entra 21'+Keys.ENTER)
sleep(10)
navegador.find_element('xpath', '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').click()
sleep(5)
navegador.find_element('xpath', '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys('uma hora vai'+Keys.ENTER)
# sleep(5)
# navegador.find_element('xpath', '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'),(+Keys.ENTER)
