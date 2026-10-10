from src.raw.extract import extract_load_api

items_dict = {
    "posts" : "/posts",
    "users" : "/users",
    "comments" : "/comments"
}

if __name__ == "__main__":

    extract_load_api(items_dict.get("comments"))

    print("Extracts concluídos com sucesso!")