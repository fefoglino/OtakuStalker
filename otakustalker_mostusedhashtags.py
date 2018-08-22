import json
from collections import Counter



def mostCommonHashtags(tweetData):
    hashtagList = []
    mostUsedHashtagsList = []

    # tweetFile = open(jsonFile, "r")
    # tweetData = json.load(tweetFile)
    # tweetFile.close()

    emptyList=[]

    for i in range(len(tweetData)):
        if (tweetData[i]["entities"]["hashtags"])==emptyList:
            continue
        else:
            for j in range(len(tweetData[i]['entities']["hashtags"])):
                hashtagList.append(tweetData[i]["entities"]["hashtags"][j]["text"])

    mostUsedHashtags=Counter(hashtagList).most_common(5)

    if len(mostUsedHashtags)<5:
        return(0)
    else:
        for i in range(5):
            mostUsedHashtagsList.append(mostUsedHashtags[i][0])
        return mostUsedHashtagsList
