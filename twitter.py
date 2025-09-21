from dotenv import load_dotenv
import os
import tweepy
import time

load_dotenv()

API_KEY = os.getenv("TWITTER_API_KEY")
API_KEY_SECRET = os.getenv("TWITTER_API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def format_tweet(product: dict, format: str) -> str:
    return 0

def send_tweet(text: str) -> int:
    try:
        api.update_status(text)
        print("Tweet sent")
        return 1
    except Exception as e:
        print(e)
    return 0
