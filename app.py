import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Meu primeiro dashboard')
st.header('Esse é um header')

abas = st.tabs(['Botão','Rádio','Dataframe','Gráfico'])

with abas[0]:
    if st.button('Clique aqui'):
        st.text('Você apertou o botão')
    
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

with abas [2]:
    caminho_arquivo = 'C:\\Users\\lucas\\PROJETOS_PYTHON\\projeto_cienciadedados_I\\frontend\\data\\ibov.csv'
    df = pd.read_csv(caminho_arquivo)
    df_novo = df[['data', 'abertura', 'maximo', 'minimo','fechamento']]
    st.dataframe(df_novo)


with abas [3]:
    plt.style.use('_mpl-gallery')

    x = 0.5 + np.arange(8)
    y= [4.8,5.5,3.5,4.6,6.5,6.6,2.6,3.0]

    fig, ax = plt.subplots()

    ax.bar(x,y, width =1, edgecolor='white', linewidth=0.7)
    ax.set(xlim=(0,8), xticks=np.arange(1,8),
        ylim=(0,8), yticks=np.arange(1,8))

    st.pyplot(fig)