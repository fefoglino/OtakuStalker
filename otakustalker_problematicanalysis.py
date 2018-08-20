import json

def probFactor(jsonFile):
    allTheTweets = str()

#     tweetFile = open(jsonFile, "r")
#     tweetData = json.load(tweetFile)
#     tweetFile.close()

    words = open("bad-words.txt", "r")
    wordsList = words.read()

    for i in range(len(tweetData)):
        allTheTweets+=tweetData[i]["text"]

    allTheTweets=allTheTweets.split() # now we have a list of every word in the tweet batch

    probCounter = 0

    for i in range(len(allTheTweets)):
        if allTheTweets[i] in wordsList:
            probCounter+=1

    probFactor = int(probCounter)/int(len(allTheTweets))
    return(probFactor)

    words.close()
