from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import urllib.request
import time

driver = webdriver.Chrome()

driver.get('https://www.amazon.com.br/s?k=livros&i=stripbooks&adgrpid=105567826925&gclid=Cj0KCQiAv8SsBhC7ARIsALIkVT0zJkdT2u6Y29mUljyVQZZ8MKkgyZHuk5dzOj8BQbvBwEBJrWJUXioaAloeEALw_wcB&hvadid=458346890782&hvdev=c&hvlocphy=1031549&hvnetw=g&hvqmt=e&hvrand=12670782735274842073&hvtargid=kwd-109570784&hydadcr=17662_11222921&tag=hydrbrgk-20&ref=pd_sl_397f2n9qav_e')

time.sleep(1.5)
driver.refresh()

books_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 's-main-slot'))
    )

books = books_section.find_elements(By.TAG_NAME, 'div')

for i in books:
    data_index = i.get_attribute('data-index')

    if data_index == '3':
        img = i.find_element(By.TAG_NAME, 'img')
        src = img.get_attribute('src')

        nome_arquivo = src.replace('https://m.media-amazon.com/images/I/', '')
        
        try:
            urllib.request.urlretrieve(src, r'C:\Users\Pedro\Downloads\EstudosPy\LibSelenium\SeleniumBasics\Arquivos_Download' + '\\' + nome_arquivo)

            print('Download concluido')
        except:
            print('Erro')

driver.quit()
