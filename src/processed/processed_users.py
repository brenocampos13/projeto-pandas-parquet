import pandas as pd

def load_json():
    
    df = pd.read_json(
        rf"C:\Users\Breno\Desktop\New folder\ANALISTA DE DADOS\Projeto_Pandas\data\raw\raw_users.json"
    )

    address = pd.DataFrame(df["address"].tolist())

    geo = pd.DataFrame(address["geo"].tolist())

    company = pd.DataFrame(df["company"].tolist())

    df["company_name"] = company["name"]
    df["company_catchPhrase"] = company["catchPhrase"]
    df["company_bs"] = company["bs"]

    df["address_street"] = address["street"]
    df["address_suite"] = address["suite"]
    df["address_city"] = address["city"]
    df["address_zipcode"] = address["zipcode"]

    df["address_geo_lat"] = geo["lat"]
    df["address_geo_lng"] = geo["lng"]

    df = df.drop(
        columns=["address", "company"]
    )

    print(df)

    df.to_csv(
        rf"C:\Users\Breno\Desktop\New folder\ANALISTA DE DADOS\Projeto_Pandas\data\processed\processed_users.csv",
        index=False
    )

if __name__ == "__main__":
    load_json()