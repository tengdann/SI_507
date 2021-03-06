from requests_oauthlib import OAuth1
import json
import sys
import requests
import secret_data # file that contains OAuth credentials
import nltk 
from nltk.corpus import stopwords
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

## SI 507 - HW5
## COMMENT WITH:
## Your section day/time:
## Any names of people you worked with on this assignment:

#usage should be python3 hw5_twitter.py <username> <num_tweets>
username = sys.argv[1]
num_tweets = sys.argv[2]

consumer_key = secret_data.CONSUMER_KEY
consumer_secret = secret_data.CONSUMER_SECRET
access_token = secret_data.ACCESS_KEY
access_secret = secret_data.ACCESS_SECRET

#Code for OAuth starts
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)
requests.get(url, auth=auth)
#Code for OAuth ends

CACHE_FNAME = "twitter_cache_improved.json"
CACHE_DICTION = {}
try:
    with open(CACHE_FNAME,'r') as cache_file:
        cache_contents = cache_file.read()
        CACHE_DICTION = json.loads(cache_contents)
        
except:
    pass

def get_from_twitter_with_cache(baseurl = 'https://api.twitter.com/1.1/statuses/user_timeline.json?', params = {}):
    global CACHE_DICTION
    tweet_list = []
    params['screen_name'] = username
    params['count'] = num_tweets
    
    if len(CACHE_DICTION) == 0:
        print("Making a request for new data...")
        # Make the request and cache the new data
        resp = requests.get(baseurl, params, auth = auth)
        CACHE_DICTION = json.loads(resp.text)
        dumped_json_cache = json.dumps(CACHE_DICTION, indent = 4)
        fw = open(CACHE_FNAME, "w", encoding = "utf-8")
        fw.write(dumped_json_cache)
        fw.close()
        for tweet in CACHE_DICTION:
            tweet_list.append(tweet['text'])
        return tweet_list
        
    else:
        print("Checking if there is any new data")
        params['since_id'] = CACHE_DICTION[0]['id']
        resp = requests.get(baseurl, params, auth = auth)
        if len(json.loads(resp.text)) != 0:
            print("New data found!")
            NEW_DICTION = {}
            NEW_DICTION = json.loads(resp.text)
            for thing in CACHE_DICTION[ :int(num_tweets) - len(json.loads(resp.text))]:
                NEW_DICTION.append(thing)
            
            dumped_json_cache = json.dumps(NEW_DICTION, indent = 4)
            fw = open(CACHE_FNAME, "w", encoding = "utf-8")
            fw.write(dumped_json_cache)
            fw.close()
            for tweet in CACHE_DICTION:
                tweet_list.append(tweet['text'])
            return tweet_list
        else:
            print("No new data. Getting cached data...")
            for tweet in CACHE_DICTION:
                tweet_list.append(tweet['text'])
            return tweet_list

#Code for Part 2:Analyze Tweets
def analyze_tweets(list_tweets):
    tokens = []
    for tweet in list_tweets:
        tokenized = nltk.word_tokenize(tweet)
        for token in tokenized:
            tokens.append(token)
            
    # FreqDist example taken from https://github.com/tistre/nltk-examples/blob/master/freqdist_top_words.py
    stop_words = set(nltk.corpus.stopwords.words('english')) # These are lowercase
    letters = "abcdefghijklmnoqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    exclusion_terms = ['http', 'https', 'RT']
    
    tokens = [token for token in tokens if token[0] in letters]
    tokens = [token for token in tokens if token not in exclusion_terms]
    
    tokens = [token.lower() for token in tokens]
    tokens = [token for token in tokens if token not in stop_words]
    
    fdist = nltk.FreqDist(tokens)
    print('USER:', username.upper())
    print('TWEETS ANALYZED:', num_tweets)
    print('5 MOST FREQUENT TWEETS:', end = ' ')
    
    for word, frequency in fdist.most_common(5):
        print(u'{}({})'.format(word, frequency), end = ' ')


if __name__ == "__main__":
    if not consumer_key or not consumer_secret:
        print("You need to fill in client_key and client_secret in the secret_data.py file.")
        exit()
    if not access_token or not access_secret:
        print("You need to fill in this API's specific OAuth URLs in this file.")
        exit()
        
    analyze_tweets(get_from_twitter_with_cache())

