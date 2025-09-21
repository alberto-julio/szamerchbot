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

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def token_call(text: str):
    return text

# def format_tweet(product: dict, format: str) -> None:
#     api.update_status()

auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def send_tweet(text: str) -> int:
    try:
        api.update_status(text)
        print("✅ Tweet sent:", text)
        return 1
    except Exception as e:
        print("❌ Error sending tweet:", e)
        return 0

# def send_tweet(text: str) -> int:
#     try:
#         response = client.create_tweet(text=text)
#         print(f"Tweet sent: {response.data}")
#         return 1
#     except Exception as e:
#         print("we failed ):")
#         print(e)
#         return 0
    
