import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Meu primeiro dashboard')
st.header('Esse é um header')

if st.button('Clique aqui'):
    st.text('Você apertou o botão')

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

# Permitir upload de arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df_novo = df[['data', 'abertura', 'maximo', 'minimo', 'fechamento']]
    
    st.dataframe(df_novo)
    
    plt.style.use('_mpl-gallery')
    
    x = 0.5 + np.arange(8)
    y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]
    
    fig, ax = plt.subplots()
    ax.bar(x, y, width=1, edgecolor='white', linewidth=0.7)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
    
    st.pyplot(fig)
