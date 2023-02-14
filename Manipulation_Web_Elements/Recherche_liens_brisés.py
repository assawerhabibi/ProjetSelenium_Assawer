import time

import requests
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
list_link=driver.find_elements(By.TAG_NAME,"a")
compteur=0
for link in list_link:
        URL=link.get_attribute("href")
        try:
            response=requests.head(URL)
        except:
            None

        if response.status_code >=400:
            print(URL,"est un lien brisé")
            compteur=compteur+1

        else:
            print(URL,"est valide")
print("le nombre de liens brisés est:",compteur)


driver.close()