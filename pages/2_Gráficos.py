import streamlit as st 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
import math
from utils.loads_dataset import loads_dataset
from utils.create_dictionary import get_data_dictionary



color_palette = sns.color_palette("YlOrRd", 5)

palette_dict = {
    "Color": "color_palette",
    "Size (cm)": "YlOrRd",
    "Weight (g)": "YlOrRd",
    "Brix (Sweetness)": "YlOrRd",
    "pH (Acidity)": "YlOrRd",
    "Softness (1-5)": "YlOrRd",
    "HarvestTime (days)": "YlOrRd",
    "Ripeness (1-5)": "YlOrRd",
    "Variety": "YlOrRd",
    "Blemishes (Y/N)": "YlOrRd",
    "Quality (1-5)": "YlOrRd",
}

color_order = ["Yellow-Orange", "Light Orange", "Orange", "Deep Orange", "Orange-Red"]

# carrgear os dados
df = loads_dataset()
data_dictionary = get_data_dictionary()

st.header("📊 Gráficos Estatístico")
st.subheader("🔹 Análise Univariada - Variáveis Qualitativas")

variaveis_qualitativas = data_dictionary.query(
    "tipo == 'Qualitativa'"
).variavel.to_list()

fig, axes = plt.subplots(figsize=(15, 6), ncols=3, nrows=1)
axes = axes.flatten()

for i, variavel in enumerate(variaveis_qualitativas):
    order = df[variavel].value_counts().index
    # Criar a figura
    ax = sns.countplot(
        df, y=variavel, ax=axes[i], order=order, alpha=0.8, color="orange"
    )
    ax.bar_label(ax.containers[0], fmt="%d", color="red", label_type="center")
    ax.set(title=f"Distribuição da variável {variavel}", xlabel="Quantidade")
    for side in ["bottom", "top", "right"]:
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_color("black")
plt.tight_layout()
st.pyplot(fig)

## variaveis Quantitativas
st.subheader("🔹 Análise Univariada - Variáveis Quantitativas")
variaveis_quantitativas = data_dictionary.query(
    "tipo == 'Quantitativa'"
).variavel.to_list()
fig, axes = plt.subplots(figsize=(8, 20), ncols=2, nrows=8)

for i, variavel in enumerate(variaveis_quantitativas):
    ax = sns.histplot(
        data=df, x=variavel, ax=axes[i, 0], kde=True, alpha=0.8, color="#ffa500"
    )
    ax.axvline(df[variavel].median(), color="blue", label="Mediana")
    ax.axvline(df[variavel].mean(), color="red", linestyle="--", label="Média")
    ax.set(title=f"Distribuição da variável {variavel}", ylabel="Quantidade")
    ax.legend()
    ax.spines["bottom"].set_color("black")
    ax.grid(False, axis="x")
    for side in ["left", "top", "right"]:
        ax.spines[side].set_visible(False)
    ax = sns.boxplot(data=df, x=variavel, ax=axes[i, 1], color="#ffa500")
    ax.set(title=f"Distribuição da variável {variavel}", ylabel="Quantidade")
    ax.spines["bottom"].set_color("black")
    ax.grid(False)


plt.tight_layout()
st.pyplot(fig)

## variaveis Quantitativas
st.subheader("🔹 Análise Bivariada - Variáveis Quantitativas")

variaveis_quantitativas = data_dictionary.query(
    "tipo == 'Quantitativa'"
).variavel.to_list()

n_combinations = math.comb(len(variaveis_quantitativas), 2)
ncols = 3
nrows = math.ceil(n_combinations / ncols)

fig, axes = plt.subplots(
    nrows=nrows, ncols=ncols, figsize=(15, 4 * nrows), squeeze=False
)
axes = axes.flatten()
combinacoes = itertools.combinations(variaveis_quantitativas, 2)

for i, (var_1, var_2) in enumerate(combinacoes):
    if i >= len(axes):
        break
    subtipos = data_dictionary.query("variavel in [@var_1, @var_2]").subtipo.unique()

    if len(subtipos) == 1:
        sns.scatterplot(data=df, x=var_1, y=var_2, ax=axes[i], color="orange")
    else:
        sns.boxplot(data=df, y=var_1, x=var_2, ax=axes[i], color="orange")

    axes[i].set_title(f"{var_1} vs {var_2}", pad=10)

for j in range(i + 1, len(axes)):
    axes[j].axis("off")

plt.tight_layout()
st.pyplot(fig)

## Correlação
st.subheader("🔹 Correlações")
corr = df.corr(numeric_only=True)

mask = np.triu(np.ones_like(corr, dtype=bool))
sns.set_style("white")

fig, ax = plt.subplots(figsize=(4, 4))

cmap = sns.diverging_palette(230, 20, as_cmap=True)

chart = sns.heatmap(
    corr,
    mask=mask,
    cmap=cmap,
    vmax=1,
    vmin=-1,
    center=0,
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.5},
    ax=ax,
    annot=True,
)
plt.tight_layout()
st.pyplot(fig)