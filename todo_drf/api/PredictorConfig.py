from django.conf import settings
import os
import preprocessor as p
from nltk.corpus import stopwords
import operator
from . import twokenizer
# from .models import Tweets, Tweets_L1
import pandas as pd
import numpy as np
import regex as re
import pickle
from sklearn.preprocessing import MultiLabelBinarizer


stop_words = set(stopwords.words('english'))

def punctuations(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    string = string.split()
    string1 = []
    for x in string:
        if x not in punctuations:
            if x.isalnum() == True:
                string1.append(x)
    string = ' '.join(string1)
    return string

def remove_stopwords(line):
    line = line.split()
    tweet = []
    for word in line:
        if word not in stop_words:
            tweet.append(word)
    return ' '.join(tweet)

def ngrams(tweet):
    tweetsenco = []
    words = tweet.split()
    for i in range(2):
        for j in range(len(words) - (i + 1)):
            tweetsenco.append(' '.join(words[j:j + i + 2]))
    return tweetsenco



class PredictorConfig():
    file_name = None
    def __init__(self, data):
        # Process the file name here
        self.file_name = data

    def operate(self):
        features = []
        with open(os.path.join(settings.MODELS, self.file_name), 'r') as f:
            for line in f:
                line = line.strip()
                features.append(line)

        direct_claim = pickle.load(open(os.path.join(settings.MODELS, 'direct_claim_classifier'), 'rb'))
        indirect_claim = pickle.load(open(os.path.join(settings.MODELS, 'indirect_claim_classifier'), 'rb'))
        opinion = pickle.load(open(os.path.join(settings.MODELS, 'opinion_classifier'), 'rb'))
        quote = pickle.load(open(os.path.join(settings.MODELS, 'quote_classifier'), 'rb'))
        not_claim = pickle.load(open(os.path.join(settings.MODELS, 'not_claim_classifier'), 'rb'))
        level_2_classifier = pickle.load(open(os.path.join(settings.MODELS, 'level_2_classifier'), 'rb'))

        def pre_processing(text):
            text = ' '.join(twokenizer.tokenizeRawTweetText(text))
            text = punctuations(text)
            text = remove_stopwords(text)
            ngram = ngrams(text)
            return ngram

        multi_hot = MultiLabelBinarizer(classes=features)

        tweets = []
        tweets_raw = []
        filename = os.path.join(settings.MODELS, 'caps_100.txt')

        with open(filename, 'r') as f:
            for line in f:
                tweets.append(line.strip().lower())
                tweets_raw.append(line.strip())
        feature = ['tweets', 'direct_claim', 'indirect_claim', 'opinion', 'quote', 'not_claim', 'level_2']
        data = pd.DataFrame(columns=feature)
        data['tweets'] = tweets

        contexts = []
        for i in data['tweets']:
            ngram = pre_processing(i)
            context = []
            for k in ngram:
                if k in features:
                    context.append(k)
            contexts.append(context)
        data['tweets_ngrams'] = contexts

        encoded_text = multi_hot.fit_transform(contexts)

        for i in range(len(encoded_text)):
            result = direct_claim.predict([encoded_text[i]])
            if result == [0]:
                data['direct_claim'][i] = 'yes'
            else:
                data['direct_claim'][i] = 'no'
            result = indirect_claim.predict([encoded_text[i]])
            if result == [0]:
                data['indirect_claim'][i] = 'yes'
            else:
                data['indirect_claim'][i] = 'no'
            result = not_claim.predict([encoded_text[i]])
            if result == [0]:
                data['not_claim'][i] = 'yes'
            else:
                data['not_claim'][i] = 'no'
            result = opinion.predict([encoded_text[i]])
            if result == [0]:
                data['opinion'][i] = 'yes'
            else:
                data['opinion'][i] = 'no'
            result = quote.predict([encoded_text[i]])
            if result == [1]:
                data['quote'][i] = 'yes'
            else:
                data['quote'][i] = 'no'

        # Push Conditioned data into the L1 DB - using the following format for all the attributes
        # ['tweets','direct_claim','indirect_claim','opinion','quote','not_claim','level_2','tweets_ngrams']
        data_l1 = data[(data['direct_claim'] == 'yes') | (data['indirect_claim'] == 'no')]
        data_l1_list = data_l1.values.tolist()

        contexts = data['tweets_ngrams']
        encoded_text = multi_hot.fit_transform(contexts)
        for i in range(len(encoded_text)):
            result = level_2_classifier.predict([encoded_text[i]])
            if result == [0]:
                data['level_2'][i] = 'fact_check'
            elif result == [1]:
                data['level_2'][i] = 'pass'

        final_data = data[data['level_2'] == 'fact_check']
        data_l2_list = final_data.values.tolist()