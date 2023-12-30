from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path='chromedriver.exe') # OBS SÓ FUNCIONARA NAS VERSÕES ANTERIORES DA v4.6.0 
driver = webdriver.Chrome(service=service) # OBS SÓ FUNCIONARA NAS VERSÕES ANTERIORES DA v4.6.0 

driver.get('https://www.youtube.com/')

time.sleep(10)
driver.quit()

# OBS SÓ FUNCIONARA NAS VERSÕES ANTERIORES DA v4.0.0 