from src.processed.processed_comments import processed_comments
from src.processed.processed_posts import processed_posts
from src.processed.processed_users import processed_users

def processed_json():

    processed_users()

    processed_posts()

    processed_comments()


if __name__ == "__main__":

    processed_json()