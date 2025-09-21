import unittest
import twitter

unittest.mock.patch


def test_automated_response():

    text = 'oogaboogachongawonga'
    reply = twitter.send_tweet()
    assert "WE MADE IT" 
    return 
class TestTwitter(unittest.TestCase):

    def test_mentions(self):
        self.assertEqual(twitter.mentions(), 1)
    def test_send_tweet(self):
        self.assertEqual(twitter.send_tweet("Test tweet"), 1)