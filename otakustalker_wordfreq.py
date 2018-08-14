import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

def makeWordCloud(jsonFile):
    allTheTweets = str()

    tweetFile = open(jsonFile, "r")
    tweetData = json.load(tweetFile)
    tweetFile.close()

    for i in range (len(tweetData)):
        allTheTweets+=tweetData[i]["text"]

    listToPrint = WordCloud().process_text(allTheTweets)

    wordCloud = WordCloud().generate_from_frequencies(listToPrint)

    plt.imshow(wordCloud, interpolation = "bilinear")
    plt.axis("off")

    plt.savefig("otakustalker_img")
    # add a return for the plot image-- image link? something?
    plt.show()
