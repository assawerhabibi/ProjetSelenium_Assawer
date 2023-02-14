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
#pour ouvrir une url on utilise la méthose get
driver.get("http://omayo.blogspot.com/")
time.sleep(4)
check_select_element=driver.find_element(By.ID,'checkbox1').is_selected()
print(check_select_element)
time.sleep(4)
check_enabled_element=driver.find_element(By.ID,'but1').is_enabled()
print(check_enabled_element)
time.sleep(3)
check_displayed_element=driver.find_element(By.ID,'hbutton').is_displayed()
print(check_displayed_element)
driver.close()