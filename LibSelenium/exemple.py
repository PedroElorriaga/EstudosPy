import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions() # INSTANCIANDO CHROMEDRIVER

def make_chrome_browse(*optionsParam):
    if optionsParam is not None:
        for option in optionsParam:
            options.add_argument(option)

    driver = webdriver.Chrome(
        options=options, # UTILIZANDO AS OPÇÕES DO CRHOME
    )

    return driver

if __name__ == '__main__':

    optionsTuple = '--disable-gpu', '--start-maximized', # CHROME OPTIONS
    browser = make_chrome_browse(*optionsTuple)

    browser.get('https://www.google.com.br')
    time.sleep(10)