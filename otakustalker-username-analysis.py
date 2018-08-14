import otakustalker_wordfreq as wf
import otakustalker_problematicanalysis as pa

pa.probFactor("tweets_small.json")

wf.makeWordCloud("tweets_small.json")
