# -*- coding: utf-8 -*-

# YouTube Video: https://www.youtube.com/watch?v=wlnx-7cm4Gg
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from twitter import Twitter, OAuth, TwitterHTTPError
import unicodedata

 
import credential


 
# # # # TWITTER STREAMER # # # #
ACCESS_TOKEN = "1008737228166594560-aGuXlq6Uqdg6AsDhGKMPm26eNAjeUV"
ACCESS_TOKEN_SECRET = "h5Xy0Te0lCxmgXLyOFXGwELF29gJtYtvxg5DjW16cgOFG"
CONSUMER_KEY = "vmYHpTCOo34lqzrWSkdnhyd10"
CONSUMER_SECRET = "4yR2GHiLQoKh71GDZgVAA8LEIJIuHT2DTMbPoOoV649rHzIpdW"

class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            en= data.encode('utf-8')
            print (en)
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ["BKK"]
    fetched_tweets_filename = "traffic.txt"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
