# theuser=input("Enter a Twitter screenname/handle to analyze ")
def usernameAnalysis(user):
    # import otakustalker_wordfreq as wf
    import otakustalker_problematicanalysis as pa
    import otakustalker_mostusedhashtags as hc
    import otakustalker_tweetfrequency as tf
    import otakustalker_totalretweets as tr
    import json
    import tweepy

    consumer_key="T3JHWaXPfk3HUeSDt7D8RxXfH"
    consumer_secret="ey2pHMJuq2kwdTbxYdMhAatohc3qYADBa91ep1zaL10a5L3Y6J"
    access_token="1029393576470474752-MsGXlLMDYdHSqPtRg0HjCgMYYEpKj7"
    access_token_secret="CAjh4EWSPIil4zGF0tKNisSSmbZVCIbwOWqBnsirK3TDY"


    userFound = False

    with open("tweets.json") as tweets:
        existingTweets = json.load(tweets)

    for i in range(len(existingTweets)):
        if existingTweets[i]["screenname"] == user:
            print("this user's tweets are already saved")
            tweetsToProcess = existingTweets[i]["tweetsByUser"]
            userFound = True
    if not userFound:
        print("Calling Twitter API")

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        userTweets = api.user_timeline(user)
        print("Tweets downloaded")
        # for tweet in public_tweets:
        #     print(tweet.text)

        for i in range(len(userTweets)):
            userTweets[i] = userTweets[i]._json
        print("Tweets converted to JSON")

        dictToDump = {}
        dictToDump["screenname"] = user
        dictToDump["tweetsByUser"] = userTweets
        tweetsToProcess = userTweets
        existingTweets.append(dictToDump)
        # listOfTweets.extend(existingTweets)

        with open("tweets.json", 'w') as f:
            json.dump(existingTweets, f)
            print("New tweets appended")




    #Analysis
    return (
    [{
    "problematicFactor": pa.probFactor(tweetsToProcess),

    "mostCommonHashtags":hc.mostCommonHashtags(tweetsToProcess),

    "tweetFrequency": tf.tweetFrequency(tweetsToProcess),

    "totalRetweets": tr.retweets(tweetsToProcess)
    }]
    )

    # wf.makeWordCloud(tweetsToProcess)
# usernameAnalysis(theuser)
