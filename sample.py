import tweepy
import json

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API 
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # This handles Twitter authentication and connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=["encryption", "internet seceurity", "data breach", "online security", "PGP", "end-to-end", "network security", "internet privacy", "hacked :(", "hacked online", "protect accounts secure", "usable design", "security user interface", "privacy user interface", "privacy account", "privacy by design", "AES", "MD5", "forward secrecy", "passowrd security", "strong password", "weak password", "security warnings", "NEAT design", "SPRUCE design", "HSTS", "machine learning security", "security network", "mobile authentication", "two factor authentication", "IoT security", "IoT privacy", "Internet of Things privacy", "Internet of Things security", "permision groups", "privacy notices", "terms of service privacy"])
