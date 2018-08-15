import otakustalker_wordfreq as wf
import otakustalker_problematicanalysis as pa
import otakustalker_mostusedhashtags as hc
import otakustalker_numberoftweets as nt

pa.probFactor("tweets_small.json")

hc.mostCommonHashtags("tweets_small.json")

nt.numberOfTweets("tweets_small.json")

wf.makeWordCloud("tweets_small.json")
