import pandas as pd

def processed_comments():
    df = pd.read_json(
        r"C:\Users\Breno\Desktop\New folder\ANALISTA DE DADOS\Projeto_Pandas\data\raw\raw_comments.json"
    )

    df["commentId"] = df["id"]

    df = df.drop(
        columns=["id"]
    )

    print(df)

    df.to_csv(
        r"C:\Users\Breno\Desktop\New folder\ANALISTA DE DADOS\Projeto_Pandas\data\processed\processed_comments.csv",
        index=False
    )

if __name__ == "__main__":
    processed_comments()