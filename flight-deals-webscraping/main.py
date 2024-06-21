from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/travel/flights?gl=BR&hl=pt-BR")

elemento_partida = driver.find_element(By.XPATH, "//input[@placeholder='Para onde?']")
time.sleep(2)
elemento_partida.send_keys("Rio de Janeiro")
#elemento_partida.send_keys(Keys.ENTER)

data_de_partida = driver.find_element(By.XPATH, "//input[@placeholder='Partida']")
data_de_partida.click()
data_de_partida.clear()
data_de_partida.send_keys("20/10/24")
data_de_partida.send_keys(Keys.ENTER)

data_de_retorno = driver.find_element(By.XPATH, "//input[@placeholder='Volta']")
data_de_retorno.click()
data_de_retorno.clear()
data_de_retorno.send_keys("30/10/24")
data_de_retorno.send_keys(Keys.ENTER)
#data_de_retorno.send_keys(Keys.ENTER)

botao_concluido = driver.find_element(By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 z18xM rtW97 Q74FEc dAwNDc']")
botao_concluido.send_keys(Keys.ENTER)

botao_busca = driver.find_element(By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc nCP5yc AjY5Oe LQeN7 TUT4y zlyfOd']")
botao_busca.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='JMc5Xc']"))
)

flights = driver.find_elements(By.XPATH, "//div[@class='JMc5Xc']")
for flight in flights:
    print(flight)

driver.quit()