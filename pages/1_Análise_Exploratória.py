import streamlit as st
import io

from utils.loads_dataset import loads_dataset
from utils.create_dictionary import get_data_dictionary



## Descrição dos Dados: descrição inicial dos dados
st.markdown("""
            ###  📌 Descrição dos dados
            O conjunto de dados tabulares contém atributos numéricos que descrevem a qualidade das laranjas, incluindo tamanho, peso, doçura (Brix), acidez (pH), maciez, época de colheita e maturação, bem como atributos categóricos como cor, variedade, presença de manchas e qualidade geral.
            ##### Link do dataset: https://raw.githubusercontent.com/atlantico-academy/datasets/refs/heads/main/orange_quality.csv
            ##### Fonte original: https://www.kaggle.com/datasets/shruthiiiee/orange-quality
            """)

# descrição das colunas
st.markdown("""
            - 📝 Colunas:
                - Size: Size of orange in cm  -> Tamanho: Tamanho da laranja em cm
                - Weight: Weight of orange in g -> Peso: Peso da laranja em g
                - Brix: Sweetness level in Brix -> Brix: Nível de doçura em Brix
                - pH: Acidity level (pH) -> pH: Nível de acidez (pH)
                - Softness: Softness rating (1-5) -> Suavidade: Classificação de suavidade (1-5)
                - HarvestTime: Days since harvest -> HarvestTime: Dias desde a colheita
                - Ripeness: Ripeness rating (1-5) -> Maturidade: Classificação de maturação (1-5)
                - Color: Fruit color -> Cor: Cor da fruta
                - Variety: Orange variety -> Variedade: Variedade de laranja
                -  Blemishes: Presence of blemishes (Yes/No) -> Manchas: Presença de manchas (Sim/Não)
                - Quality: Overall quality rating (1-5) -> Qualidade: Classificação geral da qualidade (1-5)
            """)

# carregar os dados
st.header("📂 Dataset")
df = loads_dataset()

#Exibir os primeiros dados
st.dataframe(df)

# Informações iniciais do dataset
st.header("ℹ️ Informações Iniciais")

buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

# Resumo dos dados
st.header("📊 Resumo Estatístico")
st.write(df.describe())

# mostrar o dicionario criado
# Carregar dicionário
st.header("📘 Dicionário de Dados")
data_dict = get_data_dictionary()

# Exibir o dicionário
st.dataframe(data_dict)