import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv(".env")

items_dict = {
    "/posts" : "posts",
    "/users" : "users",
    "/comments" : "comments"
}

BASE_URL = os.getenv("base_url")

def extract_api(item):
    
    response = requests.get(BASE_URL + item)

    dados = response.json()

    return dados

def to_json_api(dados, item):

    df = pd.DataFrame(dados)

    nome = items_dict.get(item)

    df.to_json(
        rf"C:\Users\Breno\Desktop\New folder\ANALISTA DE DADOS\Projeto_Pandas\data\raw\raw_{nome}.json",
        index=False
    )

def extract_load_api(item):
    
    dados = extract_api(item)
    
    to_json_api(dados, item)


if __name__ == "__main__":
    extract_load_api()