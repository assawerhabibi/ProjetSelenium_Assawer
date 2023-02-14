#ces commandes sont liés à l'application sous test
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
titre_page=driver.title
print(titre_page)
URL_page=driver.current_url
print(URL_page)
Code_source=driver.page_source
print(Code_source)

time.sleep(4)
driver.close()