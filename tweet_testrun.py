# added in another seperate test file to send out dummy tweets without fear of messing up code in main twitter fiel
import logging
import os
import time
from dotenv import load_dotenv
import tweepy

# Load credentials
load_dotenv()
logging.basicConfig(level=logging.INFO)

API_KEY = os.getenv("TWITTER_API_KEY")
API_KEY_SECRET = os.getenv("TWITTER_API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Initialize client
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def smoke_test_tweet():
    """Send a single test tweet and log the result."""
    text = f"🛠 SZA TEST TWEET AT {time.strftime('%Y-%m-%d %H:%M:%S')}"
    try:
        response = client.create_tweet(text=text)
        tweet_id = response.data.get("id")
        logging.info(f"✅ Successfully posted tweet (id={tweet_id}): {text}")
    except Exception as e:
        logging.error(f"❌ Failed to send tweet: {e}")

if __name__ == "__main__":
    smoke_test_tweet()
