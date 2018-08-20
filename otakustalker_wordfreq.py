import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud


# with open("tweets.json") as tweets:
#     existingTweets = json.load(tweets)
# for i in range(len(existingTweets)):
#     if existingTweets[i]["screenname"] == user:
#         print("this user's tweets are already saved")
#         tweetsToProcess = existingTweets[i]["tweetsByUser"]
#         # userFound = True
def makeWordCloud(user):
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

    listToPrint = WordCloud().process_text(allTheTweets)

    wordCloud = WordCloud().generate_from_frequencies(listToPrint)

    plt.imshow(wordCloud, interpolation = "bilinear")
    plt.axis("off")

    plt.savefig("otakustalker_img.png")
    # plt.show()
    # plt.close()
    # add a return for the plot image-- image link? something?
    # plt.show()
