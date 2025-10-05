from dotenv import load_dotenv
import os
import tweepy
import time
import logging


#used to load up our keys to access twitter's data and for twitter to let us use and change data through the bot account 
load_dotenv()
logging.basicConfig(level=logging.INFO)

API_KEY = os.getenv("TWITTER_API_KEY")
API_KEY_SECRET = os.getenv("TWITTER_API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

#a safe way to make sure that our bot doesnt spam tweets of something is going wrong, so it knows to stop trying
TIME_OF_LAST_TWEET = 0
COOLDOWN = 30

#also used to load our keys
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)


#test function to see if our keys worked 
def token_call(text: str):
    return text


#format on how we send tweets, can change it later if you don't like the format 
def format(product: dict) -> str:
    """Convert product info into tweet text."""
    tweet = f"{product['title']} - {product['price']}\nStatus: {product['status']}\n{product['link']} Follow @szamerchbot for more💚"
    return tweet[:280]


#the bread and butter for how we send the tweet
#takes time to send tweet so we know we are not spamming and tries to send tweet
#if successful then the tweet is sent, if not then it dies and send us an error message
def send_tweet(text: str) -> int:
    global TIME_OF_LAST_TWEET
    now = time.time()

    if now - TIME_OF_LAST_TWEET < COOLDOWN:
        logging.warning("Rate limit reached.")
        return 0
    
    try:
        client.create_tweet(text=text)
        logging.info(f"✅ Tweet sent succesfully {text}")
        TIME_OF_LAST_TWEET = now
        return 1
    except tweepy.TweepyException as e:
        logging.info(f"❌ Error: {e}")
        return 0
    
