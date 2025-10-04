import sqlite3

conn = sqlite3.connect('alunos.db')
cursor = conn.cursor()

# Cria uma tabela se não existir

cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TXT,
    nota REAL
)
''')

# Inserir dados
cursor.execute('INSERT INTO alunos (nome, nota) VALUES (?, ?)', ('Arthur', 8.0))
conn.commit() #Executar

for row in cursor.execute("SELECT * FROM alunos"):
    print(row)
conn.close()