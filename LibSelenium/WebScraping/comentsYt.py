import pandas as pd
import pathlib
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

driver.get('https://www.youtube.com/watch?v=gxLY8u3Cgxs')


driver.maximize_window()
time.sleep(4)

driver.execute_script('window.scrollBy(0, 600);')
time.sleep(2)

# CONTADOR DE COMENTARIOS
count_section = driver.find_element(By.CLASS_NAME, 'count-text')
count_int = int(count_section.find_elements(By.TAG_NAME, 'span')[0].text)

for i in range (0, count_int, 10):
    time.sleep(2)
    driver.execute_script('window.scrollBy(0, 1000);')

comments_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'contents'))
    )

# COMENTARIOS
comments = comments_section.find_elements(By.CLASS_NAME, 'ytd-item-section-renderer')

comments_texts = []
for comment in comments:
    autor = comment.find_element(By.TAG_NAME, 'yt-formatted-string')
    comments_text = comment.find_element(By.ID, 'content-text')
    comments_texts.append({'Autor: ' : autor.text, 'Comentario: ' : comments_text.text})

file_path = pathlib.Path(__file__).parent
df = pd.DataFrame(comments_texts)
data_pandas = df.to_csv('teste.txt')
