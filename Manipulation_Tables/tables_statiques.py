import time
from selenium import webdriver
#la ligne 4 et 5  vont s'occuper de télécharger chrome si il se met à jour
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#ligne 7 création d'un objet de type chrome et on l'a stocker dans une variable driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
time.sleep(4)
driver.get("https://testautomationpractice.blogspot.com/")
nombres_lignes=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print(len(nombres_lignes))
nombres_colonnes=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
print(len(nombres_colonnes))
#récupérer la valeur d'une cellule de la table
valeur_cellule=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[3]/td[1]")
print(valeur_cellule.text)
# recupérer toutes les donnés du tableau
Nb_lignes=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
Nb_colonnes=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
time.sleep(3)
# pour récupérer l'entête
V_head=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
for H in range(1,len(V_head)+1):
    data_head=driver.find_element(By.XPATH,"//table[@name='BookTable']//th["+str(H)+"]").text
    print(data_head)
time.sleep(4)
# récuperer les autres lignes on commence par 2 car on a récupérer le head
for R in range(2,Nb_lignes+1):
    for C in range(1,Nb_colonnes+1):
        valeur_cellule=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(R)+"]/td["+str(C)+"]").text
        print(valeur_cellule,end="      ")
        # pour améliorer l'affichage
    print()
