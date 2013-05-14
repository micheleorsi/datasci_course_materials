import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    words = int(0)
    frequency = {}
    for line in tweet_file:
        # parse the raw line 
        tweet_json = json.loads(line)
        # evaluate the tweet only if contains text and the lang is English
        if (u"text" in tweet_json):
            # get text and transform into lower case
            text_tweet = tweet_json[u"text"].lower()
            # for each word
            for single_word in text_tweet.split():
                # increment the total number of words
                words += int(1)
                # if the word is present add the occurrence
                if(single_word in frequency):
                    frequency[single_word] += int(1)
                # otherwise set the score of the tweet
                else:
                    frequency[single_word] = int(1)
    sorted_dic = sorted(frequency.values())
    for k, v in frequency.iteritems():
        print k.encode('utf-8'), float( v / words)

if __name__ == '__main__':
    main()
