import os
import sys
file_path = os.path.dirname(__file__)
folder_pages_path = os.path.join(file_path, '..')
sys.path.append(folder_pages_path)

import time
from BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class YoutubePage(BasePage):

    localizador_secao_titulo = (By.CLASS_NAME, 'count-text')
    localizador_quantidade_comentarios = (By.TAG_NAME, 'span')
    localizador_secao_comentarios = (By.ID, 'contents')
    localizador_comentarios = (By.CLASS_NAME, 'ytd-item-section-renderer')
    localizador_autor_id = (By.TAG_NAME, 'yt-formatted-string')
    localizador_texto_comentado = (By.ID, 'content-text')

    def __init__(self, web_driver):
        super().__init__(web_driver)


    def abrir_video_youtube(self, url):
        self.web_driver.get(url)


    def carregar_quantidade_comentarios(self):
        self.web_driver.execute_script('window.scrollBy(0, 700);')
        time.sleep(4)
        self.web_driver.execute_script('window.scrollBy(0, 500);')

    # TODO CONCERTAR BUG DESTA FUNÇÃO QUE RETORNAR O ERRO -> Message: invalid argument: 'using' must be a string
    def contar_comentarios_em_inteiros(self):
        secao_quantidade = WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located(self.localizador_secao_titulo)
        )

        return int(secao_quantidade.find_elements(self.localizador_quantidade_comentarios)[0].text.replace(',', ''))
    

    def carregar_todos_comentarios(self, callback):
        print(callback)
        for i in range (0, callback, 10):
            time.sleep(2)
            self.web_driver.execute_script('window.scrollBy(0, 1000);')

        secao_comentarios = WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located(self.localizador_secao_comentarios)
        )
    

    def listando_todos_comentarios(self, callback):
        lista_comentarios = []
        comentarios = callback.find_elements(self.localizador_comentarios)

        for comentario in comentarios:
            autor_id = comentario.find_element(self.localizador_autor_id)
            texto_comentado = comentario.find_element(self.localizador_texto_comentado)
            lista_comentarios.append({'Autor' : autor_id.text, 'Comentario' : texto_comentado.text})

        return lista_comentarios
