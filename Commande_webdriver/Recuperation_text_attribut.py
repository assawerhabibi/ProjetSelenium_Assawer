import selenium
import time

from selenium import webdriver
#la ligne 4 et 5  vont s'occuper de télécharger chrome si il se met à jour
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#ligne 7 création d'un objet de type chrome et on l'a stocker dans une variable driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#pour ouvrir une url on utilise la méthose get
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
placeholder_text=(driver.find_element(By.XPATH,"//input[@name='username']").get_attribute("placeholder"))
print(placeholder_text)
time.sleep(4)
list_link=driver.find_elements(By.TAG_NAME,'a')
time.sleep(4)
print(len(list_link))
for link in list_link:
    print(link.get_attribute('href'))

time.sleep(4)
driver.close()