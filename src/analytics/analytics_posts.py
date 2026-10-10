import pandas as pd

def merges():
    
    df = pd.read_csv(
        r"C:\Users\Breno\Desktop\New folder\ANALISTA DE DADOS\Projeto_Pandas\data\processed\processed_users.csv"
    )

    df2 = pd.read_csv(
        r"C:\Users\Breno\Desktop\New folder\ANALISTA DE DADOS\Projeto_Pandas\data\processed\processed_posts.csv"
    )

    df3 = pd.read_csv(
        r"C:\Users\Breno\Desktop\New folder\ANALISTA DE DADOS\Projeto_Pandas\data\processed\processed_comments.csv"
    )

    df2 = df2.merge(df3, "inner", left_on= "postId", right_on="postId")
    
    df = df.merge(df2, "inner", left_on="id", right_on="userId")

    print(df)

    df["user_name"] = df["name_x"]
    df["user_email"] = df["email_x"]
    df["post_body"] = df["body_x"]
    df["comment_user_name"] = df["name_y"]
    df["comment_user_email"] = df["email_y"]
    df["comment_body"] = df["body_y"]

    df = df.drop(
        columns=[
            "name_x",
            "email_x",
            "body_x",
            "name_y",
            "email_y",
            "body_y"
        ]
    )

    print(df)

    return df

def analytics_posts(df):

    comentarios_por_usuario = (
        df.groupby("user_name")["commentId"].count()
    )

    posts_por_usuarios = (
        df.groupby("user_name")["postId"].nunique()
    )

    print(comentarios_por_usuario.dtypes)
    print(posts_por_usuarios.dtypes)

    total_comentarios = comentarios_por_usuario.to_frame()
    total_comentarios = total_comentarios.reset_index()
    
    total_posts = posts_por_usuarios.to_frame()
    total_posts = total_posts.reset_index()

    total_comentarios = total_comentarios.rename(
        columns={
            "user_name":"nomeUsuario",
            "commentId":"total_comentarios"
        }
    )

    total_posts = total_posts.rename(
        columns={
            "user_name":"nomeUsuario",
            "postId":"total_posts"
        }
    )

    print(total_comentarios.dtypes)
    print(total_posts.dtypes)
    print(total_comentarios)
    print(total_posts)

    return total_comentarios, total_posts

def save_and_read_to_parquet_analytics(df1, df2):
    
    df1.to_parquet(
        r"C:\Users\Breno\Desktop\New folder\ANALISTA DE DADOS\Projeto_Pandas\data\analytics\comentarios_por_usuario.parquet",
        engine="pyarrow",
        index=None
    )
    df2.to_parquet(
        r"C:\Users\Breno\Desktop\New folder\ANALISTA DE DADOS\Projeto_Pandas\data\analytics\posts_por_usuarios.parquet",
        engine="pyarrow",
        index=None
    )

    dataframe1 = pd.read_parquet(
        r"C:\Users\Breno\Desktop\New folder\ANALISTA DE DADOS\Projeto_Pandas\data\analytics\comentarios_por_usuario.parquet"
    )

    dataframe2 = pd.read_parquet(
        r"C:\Users\Breno\Desktop\New folder\ANALISTA DE DADOS\Projeto_Pandas\data\analytics\posts_por_usuarios.parquet"
    )

    print(dataframe1)
    print(dataframe2)
    print(dataframe1.shape)
    print(dataframe1.dtypes)
    print(dataframe2.shape)
    print(dataframe2.dtypes)

if __name__ == "__main__":
    
    df = merges()

    dataframe1, dataframe2 = analytics_posts(df)

    save_and_read_to_parquet_analytics(dataframe1, dataframe2)