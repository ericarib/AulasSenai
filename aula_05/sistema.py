import csv
import time

ARQUIVO = "produtos.csv"

# Assim que executar ele verifica se o arquivo existe e cria

try:
    # x -> modelo unico de criação
    with open(ARQUIVO, "x", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Nome", "Quantidade", "Preco"])
except:
    pass 
    # Se ja existe o arquivo ele segue em frente
while True:
    nome = input("digite o nome do produto: \n")
    quantidade = int(input("digite a quantidade do Produto: \n"))
    preco = float(input("Digite o preco do produto: \n"))


    # Escrever no arquivo CSV

    with open(ARQUIVO, "a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, quantidade, preco])

    print(f'Produto {nome} adicionando com sucesso!')

    # Perguntar se deseja continuar no sistema
    continuar = input("Deseja adicionar outro produto? (s/n)")
    if continuar == "n":
        print("Encerrando sistema")
        break

    print("-" * 30) #------------------------
    time.sleep(1) #Ele vai demorar um segundo para rodar de novo 