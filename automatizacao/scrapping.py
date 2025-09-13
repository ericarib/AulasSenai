
# Biblioteca de requisição
import requests
# Responsavel por tratar o retorno
from bs4 import BeautifulSoup

# pip install requests
# pip install bs4


# Mascarar entrada no site
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

url = "https://voeazul.com.br/"

# Fazendo requisição HTTP
resposta = requests.get(url, headers=headers)

# Verificar se deu certo

if resposta.status_code == 200:
    print("Requisição feita com sucesso!")
else:
    print("Deu errado!")
    # 200 = OK

    # Traduzir a resposta do Site
    soup = BeautifulSoup(resposta.text, "html.parser")
    #  Recortar a informação
    ofertas = soup.find_all("a", class_="sc-ef69e519-0.cymzxZ")

    print("Ultimas Ofertas: ")

    for oferta in ofertas:
        print(f'{oferta.text} - {oferta['href']}')