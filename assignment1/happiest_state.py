import sys
import json
from collections import OrderedDict

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
    states = {'AL':0,'AK':0,'AS':0,'AZ':0,'AR':0,'CA':0,'CO':0,'CT':0,'DE':0,'DC':0,'FM':0,'FL':0,'GA':0,'GU':0,'HI':0,'ID':0,'IL':0,'IN':0,'IA':0,'KS':0,'KY':0,'LA':0,'ME':0,'MH':0,'MD':0,'MA':0,'MI':0,'MN':0,'MS':0,'MO':0,'MT':0,'NE':0,'NV':0,'NH':0,'NJ':0,'NM':0,'NY':0,'NC':0,'ND':0,'MP':0,'OH':0,'OK':0,'OR':0,'PW':0,'PA':0,'PR':0,'RI':0,'SC':0,'SD':0,'TN':0,'TX':0,'UT':0,'VT':0,'VI':0,'VA':0,'WA':0,'WV':0,'WI':0,'WY':0}
    # for each line in the file
    for line in tweet_file:
        # parse the raw line 
        tweet_json = json.loads(line)
        # initialize (and reset) the tweet score
        score_tweet = int(0)
        # evaluate the tweet only if contains text
        if (u"text" in tweet_json) and (u"lang" in tweet_json) and (tweet_json[u"lang"].lower() == "en") and (u"place" in tweet_json) and (tweet_json["place"] != None) and (tweet_json["place"]["country"] == "United States"):
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
            # get two digit state
            state = tweet_json["place"]["full_name"].split(", ")[1]
            if(state in states):
                states[state] += score_tweet
    ordered = OrderedDict(sorted(states.items(), key=lambda t: t[1]))
    print next(reversed(ordered))


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
