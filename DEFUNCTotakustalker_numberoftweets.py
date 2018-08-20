import json

jsonFile = "tweets_small.json"

def numberOfTweets(jsonFile):
    tweetFile = open(jsonFile, "r")
    tweetData = json.load(tweetFile)
    tweetFile.close()
    return len(tweetData)
