import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

driver.get('https://www.youtube.com/watch?v=uxUlNCmMAxE&ab_channel=GRAHAM-Topic')


driver.maximize_window()
time.sleep(4)

driver.execute_script('window.scrollBy(0, 600);')
time.sleep(2)

for i in range (0, 6):
    driver.execute_script('window.scrollBy(0, 1000);')
    

comments_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'contents'))
    )

print(comments_section)

comments = comments_section.find_elements(By.CLASS_NAME, 'ytd-item-section-renderer')
print(len(comments))

comments_texts = []
