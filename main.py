# main.py
import time
from scraper import run_scraper, load_config
from twitter import send_tweet, format

def main():
    # Load config
    config = load_config("config/config.json")

    while True:
        # Run scraper
        alerts = run_scraper(config)

        # If there are new products in stock, tweet them
        for alert in alerts:
            message = format()
            send_tweet(message)

        # Sleep between runs (you can also get this from config if you want)
        time.sleep(60)

if __name__ == "__main__":
    main()
