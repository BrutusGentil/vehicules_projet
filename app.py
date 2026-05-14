import pandas as pd
import plotly.express as px
import plotly.io as pio
import streamlit as st

# Carregando o arquivo CSV atualizado com os dados limpos e transformados para análise
car_analysis = pd.read_csv("vehicles_updated.csv")

st.header('Criação de um histograma sobre vendas de veículos')

hist_button = st.button('Clique para criar histograma')

if hist_button:
    st.write('Cria histograma relativo à venda de veículos')

    # criando um histograma
    fig = px.histogram(car_analysis, x='price')

    # exibir um gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Clique para criar gráfico de dispersão')

if scatter_button:
    st.write('Cria gráfico de dispersão relativo à venda de veículos')

    # criando um gráfico de dispersão
    fig = px.scatter(car_analysis, x='model_year', y='price')

    # exibir um gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
