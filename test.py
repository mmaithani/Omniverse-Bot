import tweepy

consumer_key='5rIQ2N7lBKijy7mucv8KO'
consumer_secret='uHpPL0GMO30krGBCS3uK1ZKToBsBvn58RoBTx9'
access_token='13192047395238543377cOzbdrAPYgd3aPLsxC'
access_token_secret='Z0lrCVFrZ23puzNw9gcve89'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
