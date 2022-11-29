from selenium import webdriver # fazer upgrade do selenium pelo pip install --upgrade
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

print("Iniciando o robô...\n")
#Para desbilitar os logs
options = webdriver.ChromeOptions()
options.add_argument("--disble-logging")
options.add_argument("--log-level=3")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://registro.br/")

#Definindo o que ele vai pesquisar
dominios = ["roboscompython.com.br", "hotmart.com.br", "uol.com.br", "pythoncurso.com.br"]

for dominio in dominios:
    pesquisar = driver.find_element(By.ID, "is-avail-field")  #mostrando para o bot onde ele vai digitar o texto
    pesquisar.clear()
    pesquisar.send_keys(dominios)
    pesquisar.send_keys(Keys.RETURN)
    time.sleep(2) #Para dar tempo da página renderizar
    driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    print("Dominio {0} {1}".format(dominio, driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong').text))

driver.close()
print("Serviço encerrado!")