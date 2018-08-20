import json

def retweets(tweetData):
    retweetCount=0
    for i in range(len(tweetData)):
        retweetCount+=tweetData[i]["retweet_count"]

    return(retweetCount)
