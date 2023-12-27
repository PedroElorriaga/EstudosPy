import os
import sys
file_path = os.path.dirname(__file__)
folder_pages_path = os.path.join(file_path, '..')
sys.path.append(folder_pages_path)

import time
from BasePage import BasePage
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class YoutubePage(BasePage, PageFactory):

    locators = {
        'localizador_quantidade_comentarios': ('CLASS_NAME', 'count-text'),
    }

    def __init__(self, web_driver):
        super().__init__(web_driver)


    def abrir_video_youtube(self, url):
        self.web_driver.get(url)


    def carregar_quantidade_comentarios(self):
        self.web_driver.execute_script('window.scrollBy(0, 700);')
        time.sleep(4)
        self.web_driver.execute_script('window.scrollBy(0, 500);')


    def contar_comentarios_em_inteiros(self):
        section_quantidade = WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'count-text'))
        )
        return int(section_quantidade.find_elements(By.TAG_NAME, 'span')[0].text.replace(',', ''))
    

    def carregar_todos_comentarios(self, callback):
        for i in range (0, callback(), 10):
            time.sleep(2)
            self.web_driver.execute_script('window.scrollBy(0, 1000);')

        section_comentarios = WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.ID, 'contents'))
        )
        
        return section_comentarios
    