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

def format(products: dict) -> str:

    #Sold Out: Taylor Swift | The Eras Tour Pink T-Shirt - S - Price: 39.15  https://store.taylorswift.com/products/the-eras-tour-pink-t-shirt VpNeed faster alerts? Check Out @popvinylsigned

    formatted_tweet = f"{products} "
    return formatted_tweet



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
    
