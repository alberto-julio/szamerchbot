import unittest
from unittest.mock import patch
import twitter

class TestTwitter(unittest.TestCase):

    def test_calls(self):
        self.assertIsNotNone(twitter.token_call(twitter.ACCESS_TOKEN))
        self.assertIsNotNone(twitter.token_call(twitter.ACCESS_TOKEN_SECRET))
        self.assertIsNotNone(twitter.token_call(twitter.API_KEY))
        self.assertIsNotNone(twitter.token_call(twitter.API_KEY_SECRET))
        self.assertIsNotNone(twitter.token_call(twitter.BEARER_TOKEN))


    @patch("twitter.api.update_status")
    def test_send_tweet(self, mock_update_status):
        # Arrange: mock update_status so it doesn’t hit Twitter
        mock_update_status.return_value = None

        # Act & Assert
        self.assertEqual(twitter.send_tweet("Test tweet"), 1)
        self.assertEqual(twitter.send_tweet("oogabooga chongawonga"), 1)

        # Confirm mock was called with expected text
        mock_update_status.assert_any_call("Test tweet")
        mock_update_status.assert_any_call("oogabooga chongawonga")

if __name__ == '__main__':
    unittest.main()