from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    'download.default_directory': r'C:\Users\Pedro\Downloads\EstudosPy\LibSelenium\SeleniumBasics\Arquivos_Download',
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True

})

driver = webdriver.Chrome(options=options)
driver.get('https://www.win-rar.com/download.html?&L=9')

btn_id = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'c7974'))
)

link_download = btn_id.find_element(By.TAG_NAME, 'a')
link_download.click()

time.sleep(5)

driver.quit()
