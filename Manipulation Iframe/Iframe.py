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
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
time.sleep(4)
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.switch_to.default_content()
time.sleep(4)
driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH,"//span[text()='WebDriver']").click()
time.sleep(4)
driver.switch_to.default_content()
time.sleep(4)
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"//a[text()='Help']").click()
time.sleep(4)


