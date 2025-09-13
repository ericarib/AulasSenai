import csv #XLSX EXCEL

# Criando um arquivo CSV

dados = [
    ["Nome", "Idade", "Cidade"],
    ["Geraldo", "25", "Cotia"],
    ["Zago", "15", "Cotia"],
    ["Julio", "21", "Cotia"]
]

# Criar CSV

with open("dados.csv", "w", newline="", encoding="utf-8") as csvarquivo:
    escritor = csv.writer(csvarquivo)
    escritor.writerows(dados)

with open("dados.csv", "r", newline="", encoding="utf-8") as csvarquivo:
    leitor = csv.reader(csvarquivo) #lendo o csv
    print("conteudo do Arquivo")
    for linha in leitor:
        print(linha)

