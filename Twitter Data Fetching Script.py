#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import tweepy as tw
import pandas as pd
#Input your keys and token
consumer_key= 'xxxxxx'
consumer_secret= 'xxxxxx'
access_token= 'xxxxxxxxxxxxxxxxxx'
access_token_secret= 'Xxxxxxx'
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)
count=0
lst=[]

# Define the search term and the date_since date as variables
search_words = "#PANGAIA"
# Collect tweets

#Tweet attributes
tId=[]
tDate=[]
tweetText=[]
rc=[]
fc=[]
favourite=[]
retweeted=[]

#User Attributes
uDate=[] 
screen_name=[]
sc=[]
followerCount=[]
friendCount=[]
userFavCount=[]




for tweet in tw.Cursor(api.search,q=search_words,lang="en").items():
        #Tweet Level
        tId.append(tweet.id)
        tweetText.append(tweet.text)
        tDate.append(tweet.created_at)
        rc.append(tweet.retweet_count)
        fc.append(tweet.favorite_count)
        favourite.append(tweet.favorited)
        retweeted.append(tweet.retweeted)
        #User level
        uDate.append(tweet.user.created_at)
        screen_name.append(tweet.user.screen_name)
        sc.append(tweet.user.statuses_count)
        followerCount.append(tweet.user.followers_count)
        friendCount.append(tweet.user.friends_count)
        userFavCount.append(tweet.user.favourites_count)
        
        

