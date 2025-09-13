from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()

driver.get("https://www.voeazul.com.br/home/br/pt/home/")
time.sleep(5)  # Dá tempo para o JS carregar

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

ofertas = soup.find_all("div", class_="sc-ef69e519-0")
for oferta in ofertas:
    destino = None
    hotel = None
    valor = None

    elementos = oferta.find_all(["p", "span", "div"])

    for el in elementos:
        texto = el.get_text(strip=True)

        if "Hotel" in texto and not hotel:
            hotel = texto
        elif "R$" in texto and not valor:
            valor = texto
        elif texto and not destino and "Hotel" not in texto and "R$" not in texto:
            destino = texto

    print(f"Destino: {destino}")
    print(f"Hotel: {hotel}")
    print(f"Valor: {valor}")
    print("-" * 40)



driver.quit()

'''
for oferta in ofertas:
    print(f"{oferta.text}")

driver.quit()
'''