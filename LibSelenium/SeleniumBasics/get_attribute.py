from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get('https://fundamentei.com/')

div_teste = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'css-117gdhw'))
    )

# <svg width="37" height="28">
width = div_teste.find_element(By.TAG_NAME, 'svg').get_attribute('width') 
height = div_teste.find_element(By.TAG_NAME, 'svg').get_attribute('height')

print('Largura: ' + width + 'px', 'Altura: ' + height + 'px')

driver.quit()
