import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

driver.get('https://books.toscrape.com')

section = driver.find_element(By.TAG_NAME, 'section')
books = section.find_elements(By.TAG_NAME, 'h3')


obeject_book = [{}, ]
for book in books:
    book_title = book.find_element(By.TAG_NAME, 'a').get_attribute('title')
    book.find_element(By.TAG_NAME, 'a').click()
    stock = driver.find_element(By.CLASS_NAME, 'instock').text
    
    livro = {
        'Título' : book_title,
        'Estoque' : stock.replace('In stock (', '').replace(' available)', '')
    } 

    obeject_book.append(livro)
    driver.back()

print(pd.DataFrame(obeject_book)) # IRA RETORNAR UMA TABELA 