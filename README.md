# 🍕 Projeto de Previsão de Preços de Pizza com Machine Learning

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red?style=for-the-badge&logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange?style=for-the-badge&logo=scikit-learn)

## 📖 Sumário
- [🌐 Site na web]()
- [📜 Descrição](#-descrição)
- [✨ Funcionalidades](#-funcionalidades)
- [💻 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [🚀 Como Executar o Projeto](#-como-executar-o-projeto)
- [🤖 Como o Código Funciona](#-como-o-código-funciona)

## 📜 Descrição
Projeto inicialmente desenvolvido pelo canal **[Daxus | empowerdata python](https://www.youtube.com/@empowerpython).**


Este projeto é uma aplicação web interativa que utiliza um modelo de **Machine Learning** para prever o preço de uma pizza com base em seu diâmetro em centímetros. A aplicação foi desenvolvida em Python e utiliza a biblioteca Streamlit para criar a interface do usuário.

O objetivo é demonstrar um ciclo completo de um projeto de Machine Learning simples, desde a leitura dos dados, treinamento do modelo, até a sua implantação em uma interface web amigável.

## ✨ Funcionalidades

-   **Previsão de Preços:** Insira o diâmetro de uma pizza e o modelo de Regressão Linear irá prever o seu valor em Reais (R$).
-   **Visualização de Dados:** Exibe um gráfico de dispersão com os dados originais e a linha de regressão aprendida pelo modelo, tornando a relação entre diâmetro e preço fácil de entender.
-   **Interface Interativa:** Interface web limpa e simples construída com Streamlit.

## 💻 Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias e bibliotecas:

-   **Linguagem:** Python
-   **Machine Learning:**
    -   **Scikit-learn:** Para criar e treinar o modelo de Regressão Linear.
-   **Manipulação de Dados:**
    -   **Pandas:** Para carregar e manipular o conjunto de dados a partir do arquivo `.csv`.
-   **Visualização de Dados:**
    -   **Matplotlib:** Para gerar o gráfico de dispersão e a linha de regressão.
-   **Interface Web:**
    -   **Streamlit:** Para criar e servir a aplicação web interativa.
-   **Gerenciamento de Dependências:**
    -   **Poetry:** Para gerenciar as bibliotecas do projeto e o ambiente virtual.

## 🤖 Como o Código Funciona 

O fluxo principal da aplicação em `app.py` é o seguinte:

1.  **Carregamento dos Dados:** O arquivo `pizzas.csv` é carregado em um DataFrame do Pandas.
2.  **Preparação dos Dados:** As colunas "diametro" (variável independente, `x`) e "preco" (variável dependente, `y`) são separadas.
3.  **Treinamento do Modelo:** Um modelo de `LinearRegression` do Scikit-learn é instanciado e treinado com os dados (`modelo.fit(x, y)`), aprendendo a relação matemática entre o diâmetro e o preço.
4.  **Criação da Interface:** O Streamlit é usado para renderizar o título, o campo de entrada numérica para o diâmetro e os botões.
5.  **Previsão e Exibição:** Quando um usuário insere um diâmetro, o método `modelo.predict()` é chamado para calcular o preço previsto, que é então formatado e exibido na tela.
6.  **Visualização Gráfica:** Um gráfico Matplotlib é gerado para mostrar os dados originais e a linha de regressão do modelo, sendo então exibido na interface com `st.pyplot()`.