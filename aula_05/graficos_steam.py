import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st

st.title ("Visualização dos dados")

# Upload do Arquivo CSV
arquivo = st.file_uploader("Envie seu arquivo CSV", type=["csv"])

# Verificar se arquivo existe
if arquivo is not None:
    # ler arquivo
    df = pd.read_csv(arquivo)

    st.write("dados carregados:")
    st.dataframe(df)

    # SELECTBOX para tipo de gráficos 
    opcao = st.selectbox(
        "Escolha o tipo de gráfico:",
        ["Barras", "Pizza", "Linha"]
    )

    # Gráfico de Barras
    if opcao == "Barras":
        st.bar_chart(df.set_index("Nome") ["Quantidade"])

    # Gráfico de linhas
    elif opcao == "Linha":
        st.line_chart(df.set_index("Nome")["Quantidade"])

    # Gráfico de Pizza
    elif opcao == "Pizza":
        st.pyplot(df.set_index("Nome").plot.pie(y="Quantidade").figure)

else:
    st.info("envie um arquivo CSV com as colunas Nome e Quantidade")