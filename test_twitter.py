import unittest
from unittest.mock import patch
import twitter

class TestTwitter(unittest.TestCase):

    @patch("twitter.client.create_tweet")
    def test_send_tweet(self, mock_create_tweet):
        # Arrange: mock create_tweet so it doesn’t hit Twitter
        mock_create_tweet.return_value = {"data": {"id": "1234567890", "text": "Test tweet"}}

        # Act & Assert
        self.assertEqual(twitter.send_tweet("Test tweet"), 1)

        twitter.TIME_OF_LAST_TWEET = 0
        self.assertEqual(twitter.send_tweet("oogabooga chongawonga"), 1)

        # Confirm mock was called with expected text
        mock_create_tweet.assert_any_call(text="Test tweet")
        mock_create_tweet.assert_any_call(text="oogabooga chongawonga")

if __name__ == '__main__':
    unittest.main()
