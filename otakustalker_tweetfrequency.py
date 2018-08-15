import json
from datetime import *

jsonFiles = "tweets_small.json"
datetimeList = []
datetimeDifferenceList = []
averagelist = []

def tweetFrequency(jsonFile):
    datetimeList = []
    tweetFile = open(jsonFile, "r")
    tweetData = json.load(tweetFile)
    tweetFile.close()

    datetimeLists = []
    for i in range(len(tweetData)):
        datetimeList.append(datetime.strptime(str(tweetData[i]["created_at"]),"%a %b %d %H:%M:%S %z %Y"))

    datetimeList=sorted(datetimeList)

    for i in range(len(datetimeList)):
        datetimeDifferenceList.append(abs(datetimeList[i]-datetimeList[i-1]).seconds/3600)

    for i in range(len(datetimeDifferenceList)):
        datetimeDifferenceList[i]=float(datetimeDifferenceList[i])

    average=sum(datetimeDifferenceList)/len(datetimeDifferenceList)
    averagelist.append(average)
    return (average)
