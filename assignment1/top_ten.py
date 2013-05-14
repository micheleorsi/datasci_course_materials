import sys
import json
from collections import OrderedDict

def main():
    tweet_file = open(sys.argv[1])
    words = int(0)
    hashtags_frequency = {}
    for line in tweet_file:
        # parse the raw line 
        tweet_json = json.loads(line)
        # evaluate the tweet only if contains entities
        if (u"entities" in tweet_json) and (tweet_json["entities"]["hashtags"]):
            for hashtag in tweet_json["entities"]["hashtags"]:
                hash = hashtag["text"]
                if(hash in hashtags_frequency):
                    hashtags_frequency[hash] += int(1)
                else:
                    hashtags_frequency[hash] = int(1)
    ordered = OrderedDict(sorted(hashtags_frequency.items(), key=lambda t: t[1]))
    for i in range(0,10):
        tuple = ordered.popitem()
        print tuple[0]+" "+str(float(tuple[1]))

if __name__ == '__main__':
    main()
