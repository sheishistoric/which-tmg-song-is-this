#! /usr/bin/env python
import json
import tweepy
import urllib3
import requests
import os

requests.packages.urllib3.disable_warnings()

cons_key = os.environ['cons_key']
cons_secret = os.environ['cons_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline('tmgbot')[0]
lastTweet = public_tweets[0].text
lastAuthor = public_tweets[0].source
lastId = public_tweets[0].id

def createTweet(string,corp):
	for i in corp:
		inc = 0
		for j in i["lyrics"]:
			inc = inc + 1
			if j.find(string) >= 0:
				album = i["album"]
				song = i["song"]
				lyrics = str(inc)
				tweet = "@tmgbot " + album + ", " + song
				# print(tweet)
				api.update_status(tweet,lastId)
				break
			else: pass

with open("tmg.json","r") as f:
	data = f.read()
	data = json.loads(data)
	data = data["tmg"]

with open("tmg.txt","r+") as g:
	line = g.readline()
if line != lastTweet and "mountain goats bot" == lastAuthor:
    g.seek(0)
    g.write(lastTweet)
    createTweet(lastTweet,data)
else:
    pass