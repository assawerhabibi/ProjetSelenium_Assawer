import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.google.com")
#driver.find_element(By.XPATH,'//input[@name="q"]').send_keys("Selenium")
#searchgoogle=driver.find_element(By.NAME,'q').send_keys("Selenium")
searchgoogle=driver.find_element(By.NAME,'q')
searchgoogle.send_keys("Selenium")
searchgoogle.submit()
#time.sleep(4)
resultat_search=driver.find_element(By.XPATH,"//h3[text()='Selenium']")
resultat_search.click()
#time.sleep(4)
driver.close()