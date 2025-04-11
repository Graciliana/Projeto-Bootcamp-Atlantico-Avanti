import pandas as pd 
import streamlit as st

# função carregar o dataset
@st.cache_resource
def loads_dataset() -> pd.DataFrame:
    return pd.read_csv(
        "https://raw.githubusercontent.com/atlantico-academy/datasets/refs/heads/main/orange_quality.csv"
    )