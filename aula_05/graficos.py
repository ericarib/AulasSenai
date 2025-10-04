import pandas  as pd
import matplotlib.pyplot as plt

ARQUIVO = "produtos.csv"
CAMPOS = ["Nome", "Quantidade", "Preco"]

df = pd.read_csv(ARQUIVO, encoding="utf-8")

df["Faturamento"] = df["Quantidade"] * df["Preco"]
print(df)

# Gráfico Boxplot
df.boxplot(column="Preco", by="Nome",grid=True)
plt.title("Distribuição de Preço por Nome")
plt.xlabel("Preco")
plt.ylabel("Produto")
plt.show()

# Gráfico de barras
df.plot(kind="bar", x="Nome", y="Preco",grid=True)
plt.title("Preço dos Produtos")
plt.xlabel("Nome")
plt.ylabel("Preco")
plt.show()

# Gráfico de pizza
df.plot(kind="area", x="Quantidade", y="Preco",grid=True)
plt.title("Quantdade por preço")
plt.xlabel("Nome")
plt.ylabel("Preco")
plt.show()