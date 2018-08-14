import json
from collections import Counter

jsonFile = "tweets_small.json"
hashtagList = []

tweetFile = open(jsonFile, "r")
tweetData = json.load(tweetFile)
tweetFile.close()

emptyList=[]

for i in range(len(tweetData)):
    if (tweetData[i]["hashtags"])==emptyList:
        continue
    else:
        for j in range(len(tweetData[i]["hashtags"])):
            hashtagList.append(tweetData[i]["hashtags"][j]["text"])

mostUsedHashtags=dict((i, hashtagList.count(i)) for i in hashtagList)
print(mostUsedHashtags)

for i in range(mostUsedHashtags):
    value=
