import tweepy
import boto3
import json
import random

def lambda_handler(event, context):

    s3 = boto3.client('s3')
    comprehend = boto3.client('comprehend')
    
    consumer_key = "//Enter Your Own Consumer Key"
    consumer_secret = "//Enter Your Own Consumer Secret Token"
    access_key = "//Enter Your Own Access Key"
    access_secret = "//Enter Your Own Access Secret"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    hashtag = event["hashtag"]
    words = "#" + hashtag
    numtweet = 100
    
    tweets = tweepy.Cursor(api.search, q=words, lang="en", tweet_mode='extended').items(numtweet)
    
    list_tweets = [tweet for tweet in tweets]
    filename = hashtag + '.json'
    dict_tweets = []
    sex = ['Male', 'Female']            #For visualization
    location = ['India', 'Australia', 'United States', 'United Kingdom', 'Singapore', 'Others']    #For visualization
    for tweet in list_tweets:
        response = comprehend.detect_sentiment(Text = tweet.full_text, LanguageCode = "en")
        tweet_dict = {
            "Hashtag" : words,
            "Date/Time" : str(tweet.created_at),
            "Name" : tweet.user.name,
            "Screen name" : tweet.user.screen_name,
            "Sex" : random.choice(sex),
            "Location" : random.choice(location),
            "Description" : tweet.full_text,
            "Sentiment" : response["Sentiment"]
        }
        #print(tweet_dict)
        #print()
        tweet_dict_copy = tweet_dict.copy()
        dict_tweets.append(tweet_dict_copy)
    s3.put_object(Body=str(dict_tweets), Bucket='test-bucket-cs474',Key=filename)

    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    temp = json.dumps(dict_tweets)
    responseObject['body'] = json.loads(temp)
    
    return responseObject