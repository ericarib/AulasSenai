
# Biblioteca de requisição
import requests
# Responsavel por tratar o retorno
from bs4 import BeautifulSoup
import time

# pip install requests
# pip install bs4


# Mascarar entrada no site
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

url = "https://www.voeazul.com.br/home/br/pt/home/"

# Fazendo requisição HTTP
resposta = requests.get(url, headers=headers)
time.sleep(5) 

# Verificar se deu certo

if resposta.status_code == 200:
    print("Requisição feita com sucesso!")

        # Traduzir a resposta do Site
    soup = BeautifulSoup(resposta.text, "html.parser")
    
    print(soup)
    #  Recortar a informação
    ofertas = soup.find_all("div", class_="sc-ef69e519-0")

    print(ofertas)

    print("Ultimas Ofertas: ")

    for oferta in ofertas:
        print(oferta)
        print(f'{oferta.find("p")}')
else:
    print("Deu errado!")
    # 200 = OK

