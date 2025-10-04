import sqlite3

conn = sqlite3.connect('livros.db')
cursor = conn.cursor()

# Cria uma tabela se não existir

cursor.execute('''
CREATE TABLE IF NOT EXISTS livros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    autor TEXT,
    ANO INTEGER
)
''')

# LOOP principal

while True:
    print("=== Cadastro de livros =====\n")
    print("1 = Cadastrar novo cliente\n")
    print("2 = listar livros\n")
    print("3 = Sair\n")

    opcao = input(" Escolha uma opção : \n")

    if opcao == "1":
            titulo = input("titulo do livro: ")
            autor = input("Qual o autor do livro: ")
            ano = int(input("Ano de publicação: "))

            cursor.execute("INSERT INTO livros (titulo, autor, ano) VALUES (?, ? , ?)",
            (titulo, autor, ano))

            conn.commit()
            print(f'Livro{titulo} criado com sucesso!')

    elif opcao == "2":
        print("Livros Cadastrados")
        for linha in cursor.execute("SELECT * FROM livros"):
            print(f'ID: {linha[0]} | Titulo {linha[1]} | Autor {linha[2]} | Ano {linha[3]}')
    elif opcao == "3":
            break
    else:
        print("Opcão inválida! tente novamente")

    