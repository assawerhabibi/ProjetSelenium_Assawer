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
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(4)
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(4)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(4)
#find elements pour trouver plusieurs éléments
#trouver tous les liens de la page
liste_liens=driver.find_elements(By.TAG_NAME,"a")
print(len(liste_liens))
time.sleep(4)
print("le texte du premier lien est :",liste_liens[3].text)
#on cherche tous les liens qui sont dans le site avec le texte
for link in liste_liens:
    print(link.text)
time.sleep(4)
driver.close()