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
    # for each line in the file
    for line in tweet_file:
        # parse the raw line 
        tweet_json = json.loads(line)
        # initialize (and reset) the tweet score
        score_tweet = int(0)
        # evaluate the tweet only if contains text
        if (u"text" in tweet_json):
            # get text and transform into lower case
            text_tweet = tweet_json[u"text"].lower()
            # for each word
	    for single_word in text_tweet.split():
                # try because I got the following errors sometimes ..
                try:
                    # compose the score tweet by adding sentiment value
                    score_tweet += int(sentiments_dictionary[single_word.encode('utf-8')])
                # catch exception and just ignore
                except (NameError, TypeError, KeyError):
                    pass
        # print always the score
        print float(score_tweet)

#Main method, manage the other ones   
def main():
    # read the sentiment file
    sent_file = open(sys.argv[1])
    # read the tweet file
    tweet_file = open(sys.argv[2])
    # perform the tweet sentiment score
    hw(load_sentiments(sent_file), tweet_file)

if __name__ == '__main__':
    main()
