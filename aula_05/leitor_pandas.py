# pip install pandas
# pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# ler o arquivo csv
df_csv = pd.read_csv("dados_pandas.csv")

# Filtrando por quantidade
df_filtrado = df_csv [df_csv['Quantidade'] > 5]
print(df_filtrado)

# Ordenando do maior para o menor
df_ordenado = df_csv.sort_values(by="Quantidade",ascending=False)
print(df_ordenado)

# Exibindo estatisticas da tabela
print(df_csv.describe())

# Criando coluna
df_csv ["faturamento"] = df_csv["Quantidade"] * df_csv["Preco"]
print(df_csv)

# Vendas
# camiseta, 70
# Camiseta, 30
media_produto = df_csv.groupby("Nome")["Preco"].mean()
print(media_produto)

# Gráfico
df_csv.boxplot(column="Preco", by="Nome", grid=True)

plt.title("Distribuição de Preço por Produto")
plt.xlabel("Nome")
plt.ylabel("Preço")

plt.show()