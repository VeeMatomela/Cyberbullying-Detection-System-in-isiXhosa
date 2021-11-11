# dependencies
import pandas as pd
import tweepy as tw
import json
import requests
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile
import datetime
from googletrans import Translator
import csv

#translater = Translator()
#out = translater.translate("sukundiqhela kakubi", dest="en")
#print(out)


def printtweetdata(n, ith_tweet):
    print()
    print(f"Tweet {n}:")
    print(f"Username:{ith_tweet[0]}")
    print(f"Tweet Text:{ith_tweet[1]}")

def scrape(words, date_since, numtweet):
    # Creating DataFrame using pandas
    db = pd.DataFrame(columns=['username', 'text'])
    # We are using .Cursor() to search through twitter for the required tweets.
    # The number of tweets can be restricted using .items(number of tweets)
    tweets = tw.Cursor(api.search, q=words,
                           since=date_since, tweet_mode='extended').items(numtweet)
    list_tweets = [tweet for tweet in tweets]
    # Counter to maintain Tweet Count
    i = 1
    # we will iterate over each tweet in the list for extracting information about each tweet
    for tweet in list_tweets:
        username = tweet.user.screen_name
        text = tweet.full_text
        # Here we are appending all the extracted information in the DataFrame
        ith_tweet = [username,text]
        db.loc[len(db)] = ith_tweet
        # Function call to print tweet data on screen
        printtweetdata(i, ith_tweet)
        i = i + 1
    filename = 'raw_data.csv'
    # we will save our database as a CSV file.
    db.to_csv(filename)

if __name__ == '__main__':
#credentials
    consumer_key = 'LZgYZq2aR3YCB4C1vxfPuKXIH'
    consumer_secret = 'qAPu1AG5neHs48KalGYxL3YwCaWOcj0ZDvsCu0HjealIACGd5x'
    access_token = '1396766344302010371-DYzdr3sinziMOvuKyp1ZnhxBegDng7'
    access_token_secret = '798RfbNlTjn7Pc4GajyAY9GA8V93D9MqMq3QgAqzRDXs7'
#authentication
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth)
# Enter Hashtag and initial date
print("Enter Twitter HashTag to search for")
words = input()
print("Enter Date since The Tweets are required in yyyy-mm--dd")
date_since = input()
# number of tweets you want to extract in one run
numtweet = 50
scrape(words, date_since, numtweet)
print('Data Successfully collected!')