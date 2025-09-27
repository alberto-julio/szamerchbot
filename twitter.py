from dotenv import load_dotenv
import os
import tweepy
import time
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

API_KEY = os.getenv("TWITTER_API_KEY")
API_KEY_SECRET = os.getenv("TWITTER_API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

TIME_OF_LAST_TWEET = 0
COOLDOWN = 30

# client = tweepy.Client(
#     bearer_token=BEARER_TOKEN,
#     consumer_key=API_KEY,
#     consumer_secret=API_KEY_SECRET,
#     access_token=ACCESS_TOKEN,
#     access_token_secret=ACCESS_TOKEN_SECRET
# )

def token_call(text: str):
    return text

def format(product: dict) -> str:
    """Convert product info into tweet text."""
    tweet = f"{product['title']} - {product['price']}\nStatus: {product['status']}\n{product['link']} Follow @szamerchbot for more."
    return tweet[:280]

def send_tweet(text: str) -> int:

    global TIME_OF_LAST_TWEET
    now = time.time()

    if now - TIME_OF_LAST_TWEET < COOLDOWN:
        logging.warning("Rate limit reached.")
        return 0

    try:
        api.update_status(text)
        logging.info(f"✅ Tweet sent succesfully {text}")
        TIME_OF_LAST_TWEET = now
        return 1
    except tweepy.TweepyException as e:
        logging.info(f"❌ Error: {e}")
        return 0
    
