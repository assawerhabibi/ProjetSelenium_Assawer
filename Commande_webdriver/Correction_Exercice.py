#import selenium
import time

from selenium import webdriver
#la ligne 4 et 5  vont s'occuper de télécharger chrome si il se met à jour
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#ligne 7 création d'un objet de type chrome et on l'a stocker dans une variable driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://google.ca")
time.sleep(5)
driver.find_element(By.NAME,"q").send_keys("selenium")
time.sleep(4)
liste_elements=driver.find_elements(By.XPATH,"//ul[@role='listbox']//li/descendant::div[@role='option']/div/span")
#time.sleep(4)
print(len(liste_elements))
time.sleep(5)
for element in liste_elements:
    if element.text=="selenium webdriver":
        element.click()
    break
time.sleep(10)
driver.close()