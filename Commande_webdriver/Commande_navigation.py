#import selenium
import time

from selenium import webdriver
#la ligne 4 et 5  vont s'occuper de télécharger chrome si il se met à jour
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#ligne 7 création d'un objet de type chrome et on l'a stocker dans une variable driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#pour ouvrir une url on utilise la méthose get
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
driver.get("https://www.google.ca")
time.sleep(4)
#back pour revenir sur le premier site (équivalent des deux flèches dasnle le navigateur )
driver.back()
time.sleep(4)
# flèche suivante
driver.forward()
time.sleep(4)
driver.refresh()
time.sleep(4)
driver.close()