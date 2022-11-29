from selenium import webdriver # fazer upgrade do selenium pelo pip install --upgrade
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import xlrd
import time

print("Iniciando o robô...\n")

#acessando o excel
excel = xlrd.open_workbook('/media/jotha/Jonathan - Arquivos/Automacao_python/dominios.xls')
planilha = excel.sheet_by_name('Plan1')
linhas = planilha.nrows
colunas = planilha.ncols 

#Para desbilitar os logs
options = webdriver.ChromeOptions()
options.add_argument("--disble-logging")
options.add_argument("--log-level=3")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://registro.br/")


for linha_atual in range(0, linhas):
    dominio = planilha.cell_value(linha_atual,0)
    pesquisar = driver.find_element(By.ID, "is-avail-field")  #mostrando para o bot onde ele vai digitar o texto
    time.sleep(1)
    pesquisar.clear()
    time.sleep(1)
    pesquisar.send_keys(dominio)
    time.sleep(1)
    pesquisar.send_keys(Keys.RETURN)    
    time.sleep(1) #Para dar tempo da página renderizar
    driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    time.sleep(1)
    print("Dominio {0} {1}".format(dominio, driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong').text))

driver.close()
print("Serviço encerrado!")