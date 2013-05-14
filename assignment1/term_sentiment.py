import sys
import json

# Load the sentiments file and returns as a dictionary
def load_sentiments(sentiment_file):
    # initialize an empty dictionary
    scores = {} 
    # for each line in the file
    for line in sentiment_file:
        #split term and score
        term, score  = line.split("\t")
        # Convert the score to an integer
        scores[term] = int(score)
    # return the populated dictionary
    return scores

# Perform the main calculus
def hw(sentiments_dictionary,tweet_file):
    sentiments_missing = {}
    # for each line/tweet in the file
    for line in tweet_file:
        # parse the raw line 
        tweet_json = json.loads(line)
        # initialize (and reset) the tweet score
        score_tweet = int(0)
        # initialize not present words
        missing_words = []
        # evaluate the tweet only if contains text and the lang is English
        if (u"text" in tweet_json) and (u"lang" in tweet_json) and (tweet_json[u"lang"].lower() == "en") :
            # get text and transform into lower case
            text_tweet = tweet_json[u"text"].lower()
            # for each word
            for single_word in text_tweet.split():
                # if the word is not present
                if(single_word not in sentiments_dictionary):
                    # append to the missing words
                    missing_words.append(single_word)
                # try because I got the following errors sometimes ..
                try:
                    # compose the score tweet by adding sentiment value
                    score_tweet += int(sentiments_dictionary[single_word.encode('utf-8')])
                # catch exception and just ignore
                except (NameError, TypeError, KeyError):
                    pass
            # create a set (without duplicates) from the list
            unique_missing_words = set(missing_words)
            # for each unique word
            for missed_word in unique_missing_words:
                # if the missed word is present add the score
                if(missed_word in sentiments_missing):
                    sentiments_missing[missed_word] += int(score_tweet)
                # otherwise set the score of the tweet
                else:
                    sentiments_missing[missed_word] = int(score_tweet)
    for k, v in sentiments_missing.iteritems():
        print k, v

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(load_sentiments(sent_file), tweet_file)
    

if __name__ == '__main__':
    main()
