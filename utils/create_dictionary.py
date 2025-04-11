import pandas as pd
import os


def get_data_dictionary(filepath="datasets/dictionary_orange.csv"):
    # Verifica se o arquivo já existe
    if os.path.exists(filepath):
        return pd.read_csv(filepath, index_col=0)
    else:
        # Criação do dicionário de dados
        data_dictionary = pd.DataFrame(
            [
                {
                    "variavel": "Size (cm)",
                    "descrição": "Tamanho da laranja em (cm)",
                    "tipo": "Quantitativa",
                    "subtipo": "Continua",
                },
                {
                    "variavel": "Weight (g)",
                    "descrição": "Peso da laranja em (g)",
                    "tipo": "Quantitativa",
                    "subtipo": "Continua",
                },
                {
                    "variavel": "Brix (Sweetness)",
                    "descrição": "Teor de açúcar / Doçura",
                    "tipo": "Quantitativa",
                    "subtipo": "Continua",
                },
                {
                    "variavel": "pH (Acidity)",
                    "descrição": "Nível de acidez",
                    "tipo": "Quantitativa",
                    "subtipo": "Continua",
                },
                {
                    "variavel": "Softness (1-5)",
                    "descrição": "Maciez",
                    "tipo": "Quantitativa",
                    "subtipo": "Discreta",
                },
                {
                    "variavel": "HarvestTime (days)",
                    "descrição": "Tempo decorrido após a colheita",
                    "tipo": "Quantitativa",
                    "subtipo": "Discreta",
                },
                {
                    "variavel": "Ripeness (1-5)",
                    "descrição": "Escala de maturação",
                    "tipo": "Quantitativa",
                    "subtipo": "Discreta",
                },
                {
                    "variavel": "Color",
                    "descrição": "Cor da laranja",
                    "tipo": "Qualitativa",
                    "subtipo": "Nominal",
                },
                {
                    "variavel": "Variety",
                    "descrição": "Variedade da laranja",
                    "tipo": "Qualitativa",
                    "subtipo": "Nominal",
                },
                {
                    "variavel": "Blemishes (Y/N)",
                    "descrição": "Presença de manchas na laranja",
                    "tipo": "Qualitativa",
                    "subtipo": "Nominal",
                },
                {
                    "variavel": "Quality (1-5)",
                    "descrição": "Qualidade da laranja",
                    "tipo": "Quantitativa",
                    "subtipo": "Discreta",
                },
            ]
        )
        # Salvar o dicionário
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        data_dictionary.to_csv(filepath)
        return data_dictionary
