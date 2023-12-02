import time

from selenium import webdriver

options = webdriver.ChromeOptions() # INSTANCIANDO CHROMEDRIVER
options.add_argument(
    '--start-maximized', # OPÇÃO DE INICIAR COM A TELA CHEIA
) 

driver = webdriver.Chrome(
    options=options, # UTILIZANDO AS OPÇÕES DO CRHOME
)

driver.get('https://www.google.com.br')
time.sleep(10)