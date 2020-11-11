import tweepy
import random
from time import sleep
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,timeout=150,retry_count=5)

# Where q='#example', change #example to whatever hashtag or keyword you want to search.
# Where items(5), change 5 to the amount of retweets you want to tweet.

# Where On Earth ID for india is 23424848.

# numberList = [23424848,1]

while True:
    api = tweepy.API(auth,timeout=150)

    # WOE_ID=random.choice(numberList)
    WOE_ID = 23424848

    india_trends = api.trends_place(WOE_ID)

    for i in range(10):
      hashtag = india_trends[0]["trends"][i]["name"]
      print("tweeting -> ",hashtag)

      for tweet in tweepy.Cursor(api.search, q=hashtag,result_type="mixed",lang='en').items(1):

          try:
              print('Retweet Bot found--> ',hashtag,' <-- tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')

              tweet.favorite()
              tweet.retweet()

              print("Successfull !\n")
              sleep(300)

          except tweepy.TweepError as error:
                        print('Not successful. Reason: ')
                        print(error.reason,"\n")

                        sleep(960)
          except:
            continue


