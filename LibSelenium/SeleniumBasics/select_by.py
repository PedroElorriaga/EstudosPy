from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()

driver.get('https://www.imdb.com/chart/top/')

time.sleep(2)
driver.execute_script('window.stop();')

sort_by = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'sort-by-selector'))
)

# DOCUMENTAÇÃO PARA O SELECT https://www.selenium.dev/pt-br/documentation/webdriver/support_features/select_lists/
select = Select(sort_by)
select.select_by_value('RELEASE_DATE')


time.sleep(8)
driver.quit()
