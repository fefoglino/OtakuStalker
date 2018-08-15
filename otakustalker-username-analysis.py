import otakustalker_wordfreq as wf
import otakustalker_problematicanalysis as pa
import fixingHashtagCounter as hc

pa.probFactor("tweets_small.json")

hc.mostCommonHashtags("tweets_small.json")

wf.makeWordCloud("tweets_small.json")
