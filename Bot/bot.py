from httplib2 import Authentication
import tweepy
import os

#print (os.getcwd())
os.chdir('/home/leon/Desktop/Code/Py/twitterBot')

file_name = 'twitt.txt'
all_keys = open(file_name, 'r').read().splitlines()
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator)


# updates my profile desription
api.update_profile(description = 'Testing my Twitter bot')