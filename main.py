from src.raw.extract import extract_load_api
from src.processed.processed import processed_json
from src.analytics.analytics_posts import analytics

items_dict = {
    "posts" : "/posts",
    "users" : "/users",
    "comments" : "/comments"
}

if __name__ == "__main__":

    extract_load_api(items_dict.get("comments"))

    print("Extracts concluídos com sucesso!")

    processed_json()

    print("Dados processados com sucesso!")

    analytics()

    print("Arquivos salvos em .parquet com sucesso!")