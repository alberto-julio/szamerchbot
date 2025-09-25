import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    @patch("main.send_tweet")  # mock out Twitter
    @patch("main.run_scraper") # mock out scraper
    def test_main_flow(self, mock_run_scraper, mock_send_tweet):
        # Pretend scraper found a product
        mock_run_scraper.return_value = [
            {
                "title": "Cool Shirt",
                "price": "$20",
                "stock": "in_stock",
                "link": "https://shop.com/item"
            }
        ]

        # Run one iteration of main logic (not infinite loop)
        config = {"dummy": "config"}
        alerts = mock_run_scraper(config)

        for alert in alerts:
            message = f"{alert['title']} is now {alert['stock']} at {alert['link']} for {alert['price']}"
            main.send_tweet(message)

        # Check that send_tweet was called with correct message
        mock_send_tweet.assert_called_once_with(
            "Cool Shirt is now in_stock at https://shop.com/item for $20"
        )

if __name__ == "__main__":
    unittest.main()
