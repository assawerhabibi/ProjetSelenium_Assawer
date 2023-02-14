import time
from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#driver.implicitly_wait(20)
# creation d'un objet qui gere la synchronisation
MyWait=WebDriverWait(driver,20,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
driver.get("https://www.google.com")
#driver.find_element(By.XPATH,'//input[@name="q"]').send_keys("Selenium")
#searchgoogle=driver.find_element(By.NAME,'q').send_keys("Selenium")
#searchgoogle=driver.find_element(By.NAME,'q')
searchgoogle=MyWait.until(EC.presence_of_element_located((By.NAME,'q')))
searchgoogle.send_keys("Selenium")
searchgoogle.submit()
#time.sleep(4)
#resultat_search=driver.find_element(By.XPATH,"//h3[text()='Selenium']")
#EC=
resultat_search=MyWait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
resultat_search.click()
#time.sleep(4)
driver.close()