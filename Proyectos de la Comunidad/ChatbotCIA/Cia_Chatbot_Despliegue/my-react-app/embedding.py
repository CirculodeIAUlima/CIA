import sys
import openai
import os
from num2words import num2words
import os
import pandas as pd
import numpy as np
from openai.embeddings_utils import get_embedding, cosine_similarity

API_KEY = "f6fba7125b754c0d93f2fce1da3a43a3"
RESOURCE_ENDPOINT = "https://ciaulima.openai.azure.com/"
openai.api_type = "azure"
openai.api_key = API_KEY
openai.api_base = RESOURCE_ENDPOINT
openai.api_version = "2022-12-01"

df = pd.read_csv('bills.csv')

df['ada_v2'] = df["text"].apply(lambda x : get_embedding(x, engine='ada002cia'))

def search_docs(df, user_query, top_n=3, to_print=False):
    embedding = get_embedding(
        user_query,
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

# Read the input from stdin
user_query = input()

# Perform the search
res = search_docs(df, user_query, top_n=3)
first_row = res.iloc[0]
text_value = first_row['text']

# Write the output to stdout with UTF-8 encoding
sys.stdout.buffer.write(text_value.encode('utf-8'))
