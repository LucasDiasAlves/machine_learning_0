import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()

x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)


st.title("Prevendo o valor de uma pizza🍕")

st.divider()
diametro = st.number_input("Digite o tamanho do diametro de sua pizza 😋: ", format="%.2f")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    preco_formatado_com_virgula = f"{preco_previsto:.2f}".replace('.', ',')

    st.write(f"O valor de sua pizza com o diâmetro de {diametro:.2f} cm é de R${preco_formatado_com_virgula}!")
    

    
st.divider()

st.title("Gráfico")
st.text("Relação dos diâmetros das pizzas e seus valores")
fig, ax = plt.subplots()

ax.scatter(x, y, color='blue', label='Dados Originais')

ax.plot(x, modelo.predict(x), color='red', linewidth=2, label='Linha de Regressão (Previsão)')

ax.set_xlabel("Diâmetro (cm)")
ax.set_ylabel("Preço (R$)")
ax.set_title("Análise de Preço da Pizza por Diâmetro")
ax.legend()
ax.grid(True)

st.pyplot(fig)