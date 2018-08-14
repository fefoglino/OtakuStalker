import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

def makeWordCloud(jsonFile):
    twitterCompleteData = jsonFile #change this when project gets approved

    allTheTweets = str()

    tweetFile = open(twitterCompleteData, "r")
    tweetData = json.load(tweetFile)
    tweetFile.close()

    for i in range (len(tweetData)):
        allTheTweets+=tweetData[i]["text"]

    listToPrint = WordCloud().process_text(allTheTweets)

    wordCloud = WordCloud().generate_from_frequencies(listToPrint)

    plt.imshow(wordCloud, interpolation = "bilinear")
    plt.axis("off")

    plt.savefig("otakustalker_img")
    plt.show()
