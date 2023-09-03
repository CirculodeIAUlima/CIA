import openai
import os
import re
import requests
import sys
from num2words import num2words
import os
import pandas as pd
import numpy as np
from openai.embeddings_utils import get_embedding, cosine_similarity
import tiktoken

API_KEY = "f6fba7125b754c0d93f2fce1da3a43a3"
RESOURCE_ENDPOINT = "https://ciaulima.openai.azure.com/"

openai.api_type = "azure"
openai.api_key = API_KEY
openai.api_base = RESOURCE_ENDPOINT
openai.api_version = "2022-12-01"

df = pd.read_csv('bills.csv')

df['ada_v2'] = df["text"].apply(lambda x : get_embedding(x, engine = 'ada002cia'))

#IF 'to_print' is set to True, the function will also print the obtained ROWS, else it won't
def search_docs(df, user_query, top_n=3, to_print=False):
    embedding = get_embedding(
        user_query,
        #engine="text-embedding-ada-002" engine debe ser identico al deployment name del modelo
		engine="ada002cia"
    )
    df["similarities"] = df.ada_v2.apply(lambda x: cosine_similarity(x, embedding))

    res = (
        df.sort_values("similarities", ascending=False)
        .head(top_n)
    )
    if to_print:
        print(res)
    return res

user_query = input("Ingresar el texto: ")
res = search_docs(df, user_query, top_n=3) # Aqui va la pregunta a realizar y se muestran resultados con mas similitud
first_row = res.iloc[0]  # Selecciona la primera fila del df
text_value = first_row['text']  # Extraer el valor de la columna 'text'
print('Respuesta obtenida por parte del modelo:')
print(text_value)