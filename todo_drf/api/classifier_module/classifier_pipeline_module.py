
# coding: utf-8

import preprocessor as p
from nltk.corpus import stopwords 
import operator
from classifier_module import twokenizer
# import twokenizer
import pandas as pd
import numpy as np
import regex as re
import pickle
from sklearn.preprocessing import MultiLabelBinarizer


"""
Classification module
"""
class Classifier:
    """
        To Identify tweets into factcheck-worthy

        Input : - streaming tweets
        Return :- different class of tweets which are factcheck-worthy
        and the input of google search api : dataframe
        """

    def __init__(self):
        self.Dir_name = "./"
        self.direct_claim = pickle.load(open(self.Dir_name+'direct_claim_classifier', 'rb'))
        self.indirect_claim = pickle.load(open(self.Dir_name+'indirect_claim_classifier', 'rb'))
        self.opinion = pickle.load(open(self.Dir_name+'opinion_classifier', 'rb'))
        self.quote = pickle.load(open(self.Dir_name+'quote_classifier', 'rb'))
        self.not_claim = pickle.load(open(self.Dir_name+'not_claim_classifier', 'rb'))
        self.level_2_classifier = pickle.load(open(self.Dir_name+'level_2_classifier', 'rb'))



    def punctuations(self,string):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        string=string.split()
        string1=[]
        for x in string:
            if x not in punctuations:
                if x.isalnum() == True:
                    string1.append(x)
        string=' '.join(string1)
        return string


    def remove_stopwords(self,line):
        stop_words = set(stopwords.words('english'))
        line=line.split()
        tweet=[]
        for word in line:
            if word not in stop_words:
                tweet.append(word)
        return ' '.join(tweet)


    def ngrams(self,tweet):
        tweetsenco=[]
        words=tweet.split()
        for i in range(2):
            for j in range(len(words)-(i+1)):
                tweetsenco.append(' '.join(words[j:j+i+2]))
        return tweetsenco


    def pre_processing(self,text):
        text=' '.join(twokenizer.tokenizeRawTweetText(text))
        text=self.punctuations(text)
        text=self.remove_stopwords(text)
        ngram=self.ngrams(text)
        return ngram

    def prediction(self, filename):
        features = []
        with open('classifiers_features.txt', 'r') as f:
            for line in f:
                line = line.strip()
                features.append(line)
        multi_hot = MultiLabelBinarizer(classes=features)
        tweets = []
        with open(filename, 'r') as f:
            for line in f:
                tweets.append(line.strip().lower())
        feature = ['tweets', 'direct_claim', 'indirect_claim', 'opinion', 'quote', 'not_claim', 'level_2']
        data = pd.DataFrame(columns=feature)
        data['tweets'] = tweets
        contexts = []
        for i in data['tweets']:
            ngram = self.pre_processing(i)
            context = []
            for k in ngram:
                if k in features:
                    context.append(k)
            contexts.append(context)
        data['tweets_ngrams'] = contexts
        encoded_text = multi_hot.fit_transform(contexts)

        for i in range(len(encoded_text)):
            result = self.direct_claim.predict([encoded_text[i]])
            if result == [0]:
                data['direct_claim'][i] = 'yes'
            else:
                data['direct_claim'][i] = 'no'
            result = self.indirect_claim.predict([encoded_text[i]])
            if result == [0]:
                data['indirect_claim'][i] = 'yes'
            else:
                data['indirect_claim'][i] = 'no'
            result = self.not_claim.predict([encoded_text[i]])
            if result == [0]:
                data['not_claim'][i] = 'yes'
            else:
                data['not_claim'][i] = 'no'
            result = self.opinion.predict([encoded_text[i]])
            if result == [0]:
                data['opinion'][i] = 'yes'
            else:
                data['opinion'][i] = 'no'
            result = self.quote.predict([encoded_text[i]])
            if result == [1]:
                data['quote'][i] = 'yes'
            else:
                data['quote'][i] = 'no'

        data_l2 = data[data['not_claim'] != 'yes']
        contexts = data['tweets_ngrams']
        encoded_text = multi_hot.fit_transform(contexts)
        for i in range(len(encoded_text)):
            result = self.level_2_classifier.predict([encoded_text[i]])
            if result == [0]:
                data['level_2'][i] = 'fact_check'
            elif result == [1]:
                data['level_2'][i] = 'pass'

        final_data = data[data['level_2'] == 'fact_check']
        return final_data["tweets"]





if __name__ == '__main__':
    filename = './Test_svm.txt'
    classifier = Classifier()
    predict = classifier.prediction(filename)
    print(predict)



