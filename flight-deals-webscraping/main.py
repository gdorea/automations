from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com/travel/flights?gl=BR&hl=pt-BR")

elemento_partida = driver.find_element(By.CLASS_NAME, "II2One j0Ppje zmMKJ LbIaRd")
elemento_partida.click()
elemento_cidade1 = driver.find_element(By.CLASS_NAME, "zsRT0d")
elemento_cidade1.click()
sleep(2)
elemento_partida.send_keys(Keys.TAB)
sleep(2)
elemento_partida.send_keys("Rio de Janeiro")


