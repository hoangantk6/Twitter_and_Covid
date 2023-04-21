from __future__ import unicode_literals
# https://github.com/sixohsix/twitter/tree/master
# Python Twitter Tool (Version 1.18.0)
from twitter import *
from twitter.stream import TwitterStream, Timeout, HeartbeatTimeout, Hangup
import time
import json

# Replace with your own key/secret
consumer_key = 'UazoeRjN2CuN8pA6vHLc7WUxU'
consumer_secret = 'Q5BakeUlBYQ7RfNipZWTuwUoOKmWXx3nzIoMzOXn2ZsVax3xI0'
#AAAAAAAAAAAAAAAAAAAAAAXnVwEAAAAAPWr%2BL5tQ9uPEVHj2Nr2TMVzJQss%3DoC2BwtUpF1VN2LcsVui3VD2p89SS8HACnDNS1cBTtiwh3eUy6D
resource_owner_key = '1452901469921832962-Vh017wqh4EbBwHrjVHtJ57p4iKGCHG'
resource_owner_secret = 'TwzWyKE9d2A2A8Ag3inMAh8gnybsb6td73XS7Jifnueat'
filename = 'data.json'


if __name__ == '__main__':
    while True:
        try:
            # When using twitter stream you must authorize.
            auth = OAuth(
                consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                token=resource_owner_key,
                token_secret=resource_owner_secret
            )
            # Set location bounding box
            query_args = {'track': '#covid2019,#covid-19,#coronavirus, #vaccine, #vaccination, #getvaccinated, #DeltaVariant,#Pfizer,#Moderna, #AstraZeneca,#Janssen,#COVID, #verocell', 'stall_warnings':True}
            # Start authorization and filtering tweets
            stream = TwitterStream(auth=auth)
            tweet_iter = stream.statuses.filter(**query_args)

            # Iterate over the sample stream.
            for tweet in tweet_iter:
                # We should check the type of tweet.
                # It might be  a delete or data message.
                if tweet is None:
                    print("-- None --")
                elif tweet is Timeout:
                    print("-- Timeout --")
                elif tweet is HeartbeatTimeout:
                    print("-- Heartbeat Timeout --")
                elif tweet is Hangup:
                    print("-- Hangup --")
                else:
                    print(tweet)
                    #with open('data.json', 'w', encoding='utf-8') as f:
                        #json.dump(tweet, f)
                    # 1. Read file contents
                    with open(filename, 'a') as json_file:
                        json.dump(tweet, json_file,
                                  indent=4)




                    #df = pd.DataFrame(tweet['id'],tweet['text'],tweet['user'],tweet['place'],tweet['quoted_status'],str(tweet['retweeted_status']), str(tweet['entities']),tweet['lang'],tweet['timestamp_ms'] )
                    #df.to_csv('data.csv')




        except Exception as e:
            print('error (Follow): ' + str(e))
            time.sleep(15)
