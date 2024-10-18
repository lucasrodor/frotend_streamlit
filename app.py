import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Definir o caminho do arquivo CSV
caminho = Path(__file__).resolve().parent

st.title('Meu primeiro dashboard')
st.header('Esse é um header')

# Criar as abas do Streamlit
abas = st.tabs(['Botão', 'Rádio', 'Dataframe', 'Gráfico'])

# Aba 1 - Botão
with abas[0]:
    if st.button('Clique aqui'):
        st.text('Você apertou o botão')

# Aba 2 - Rádio
with abas[1]:
    opcao = st.radio(
        'Escolha uma opção:',
        ('Flamengo', 'Corinthians', 'Palmeiras')
    )

    if opcao == 'Flamengo':
        st.info('Você é campeão!')
    elif opcao == 'Corinthians':
        st.warning('Você é gambá!')
    elif opcao == 'Palmeiras':
        st.error('Você é um perdedor!')

# Aba 3 - DataFrame
with abas[2]:
    if caminho.exists():
        # Carregar o arquivo CSV
        df = pd.read_csv(str(caminho) + "/data/ibov.csv")
        df_novo = df[['data', 'abertura', 'maximo', 'minimo', 'fechamento']]
        st.dataframe(df_novo)

# Aba 4 - Gráfico
with abas[3]:
    # Gráfico do preço de fechamento do IBOVESPA
    st.title('Gráfico de Preço de Fechamento do IBOVESPA')

    # Converter a coluna 'data' para o formato datetime
    df_novo['data'] = pd.to_datetime(df_novo['data'])

    # Criar o gráfico de linha
    plt.figure(figsize=(10, 6))
    plt.plot(df_novo['data'], df_novo['fechamento'], label='Fechamento', color='blue')

    plt.title('Preço de Fechamento do IBOVESPA ao longo do tempo')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento (R$)')
    plt.grid(True)
    plt.legend()

    # Exibir o gráfico no Streamlit
    st.pyplot(plt)
