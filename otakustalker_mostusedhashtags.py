import json
from collections import Counter


jsonFile = "tweets_small.json"

def mostCommonHashtags(jsonFile):
    hashtagList = []
    mostUsedHashtagsList = []

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

    mostUsedHashtags=Counter(hashtagList).most_common(5)

    for i in range(5):
        mostUsedHashtagsList.append(mostUsedHashtags[i][0])
    print(mostUsedHashtagsList)
    return mostUsedHashtagsList
