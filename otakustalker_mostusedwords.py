import json
from collections import Counter
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

def mostCommonWords(user):
    with open("tweets.json") as tweets:
        existingTweets = json.load(tweets)
    for i in range(len(existingTweets)):
        if existingTweets[i]["screenname"] == user:
            print("this user's tweets are already saved")
            tweetsToProcess = existingTweets[i]["tweetsByUser"]
    allTheTweets = str()

    # tweetFile = open(jsonFile, "r")
    # tweetData = json.load(tweetFile)
    # tweetFile.close()

    for i in range(len(tweetsToProcess)):
        allTheTweets+=tweetsToProcess[i]["text"]

    listToCount = WordCloud().process_text(allTheTweets)

    mostUsedWordsList=[]

    mostUsedWords=Counter(listToCount).most_common(50)

    if len(mostUsedWords)<50:
        return(0)
    else:
        for i in range(50):
            mostUsedWordsList.append(mostUsedWords[i][0])
        return mostUsedWordsList

# import json
# from collections import Counter
#
# jsonFile="tweets.json"
#
# def mostCommonWords(jsonFile):
#     wordsListofLists = []
#     wordsList = []
#     mostUsedWordsList = []
#
#     tweetFile = open(jsonFile, "r")
#     tweetData = json.load(tweetFile)
#     tweetFile.close()
#
#     print(tweetData[0]["tweetsByUser"][0]["text"]) #this is what the code will pass into the function(?)
#
#
#     for i in range(len(tweetData)):
#         wordsListofLists.append(tweetData[i]["tweetsByUser"][0]["text"])
#         wordsListofLists[i]=wordsListofLists[i].split()
#
#     for i in range(len(wordsListofLists)):
#         for j in range(len(wordsListofLists[i])):
#             wordsList.append(wordsListofLists[i][j])
#
#     mostUsedWords=Counter(wordsList).most_common(50)
#
#     if len(mostUsedWords)<50:
#         return("Not enough words to analyze")
#     else:
#         for i in range(50):
#             mostUsedWordsList.append(mostUsedWords[i][0])
#         return mostUsedWordsList
#
# mostCommonWords(jsonFile)
