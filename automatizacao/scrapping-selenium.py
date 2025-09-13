# pip install selenium
# pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


# configurar navegador

options = webdriver.ChromeOptions()

# Mascarar que não somos uma automação
options.add_argument('--disable-blink-features=AutomationControlled')
# Mascarar o UserAgent que vai acessar o site
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/91.0.4472.124 Safari/537.36')

driver = webdriver.Chrome(options=options)

url = "https://www.webmotors.com.br/carros/sp-cotia/volkswagen/golf?tipoveiculo=carros"

driver.get(url)

time.sleep(5) # esperar 5 seg para carregar o site

# Extrair os dados

carros = driver.find_elements(By.CLASS_NAME, 'Container_70j0p_1')
for carro in carros:
    nome = carro.find_element(By.CLASS_NAME, '_web-title-medium_qtpsh_51').text
    preco =carro.find_element(By.CLASS_NAME, '_body-bold-large_qtpsh_78').text

    print(f'Nome do carro: {nome}')
    print(f'preço do carro: {preco}')

