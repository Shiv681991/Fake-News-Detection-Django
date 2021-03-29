
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

'''
For demo
Input : 1 tweet
Procedure : Use google_search_api.py to obtain 10 urls and corresponding News contents
Use alBERT SQuAD Q&A to obtain sentence to entail
User BERT_Large to obtain sentence similarity summary
Need to check for headlines-- Ask Purabi for obtaining headlines as well.
get 6 entailment outputs and
Output : Check if it is entailed or not


'''
import pandas as pd
import csv
import torch
from question_answering import QuestionAnsweringModel
import collections
import json
import numpy as np
import os
import re
import string
import json
import matplotlib.pyplot as plt
import matplotlib
from re import search
import nltk
import scipy
import spacy
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from sentence_transformers import SentenceTransformer
from tabulate import tabulate
import time
from google_search_api import content_extraction_from_tweet
roberta = torch.hub.load('pytorch/fairseq', 'roberta.large.mnli')
roberta.eval()  # disable dropout for evaluation
result_labels = ["contradiction", "neutral", "entailment"]


# Utility modules/defs
def convert_qa_2_squad(paragraph, question):
    dev_data = {
        "version": "v2.0",
        "data": [
            {
                "title": "TestQuestion",
                "paragraphs": [
                    {
                        "qas": [
                            {
                                "question": "Any Question?",
                                "id": "Bob_Chait",
                                "answers": [
                                    {
                                        "text": "Any_answer is Fine",
                                        "answer_start": 170
                                    }
                                ],
                                "is_impossible": False
                            }
                        ],
                        "context": "Any Paragraph here"
                    }
                ]
            }
        ]
    }
    for datum in dev_data["data"]:
        for para in datum["paragraphs"]:
            # print(para["context"])
            para["context"] = paragraph
            for qa in para["qas"]:
                qa["question"] = question
    with open('result.json', 'w') as fp:
        json.dump(dev_data, fp)
    return dev_data

def get_QnA_sentence_to_entail(paragraph, tweet):
    dev_data = convert_qa_2_squad(paragraph, tweet)
    dev_data = [item for topic in dev_data['data'] for item in topic['paragraphs']]
    model_albert_large_v1 = QuestionAnsweringModel('albert',
                                                   './models/model_albert_large_v1_outputs')
    preds = model_albert_large_v1.predict(dev_data)
    albert_answer = preds[0]['answer']
    corpus = nltk.sent_tokenize(paragraph)
    for idx in range(len(corpus)):
        fullstring = corpus[idx]  # +corpus[idx+1]
        if fullstring.find(albert_answer):
            return fullstring
        else:
            pass


similar_sentences_embedder = SentenceTransformer('bert-base-nli-mean-tokens')


def get_similar_sentences(paragraph, tweet, similar_sentences_embedder, closest_n=3):
    corpus = nltk.sent_tokenize(paragraph)
    corpus_embeddings = similar_sentences_embedder.encode(corpus)
    queries = nltk.sent_tokenize(tweet)
    query_embeddings = similar_sentences_embedder.encode(queries)
    for query, query_embedding in zip(queries, query_embeddings):
        distances = scipy.spatial.distance.cdist([query_embedding], corpus_embeddings, "cosine")[0]
        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1])
        similar_sents = []
        for idx, distance in results[0:closest_n]:
            similar_sents.append(corpus[idx].strip())
        return (" ".join(similar_sents))


def all_entaliments_at_once(tweet, news_content, headline):
    #   get_QnA_sentence_to_entail(context,question)
    tweet = nltk.word_tokenize(tweet)
    news_content = nltk.word_tokenize(news_content)
    headline = nltk.word_tokenize(headline)
    headline_n_newscontent = headline + news_content
    headline_n_newscontent = " ".join(headline_n_newscontent).strip()
    news_content = " ".join(news_content).strip()
    headline = " ".join(headline).strip()
    tweet = " ".join(tweet).strip()
    only_qna_extract = get_QnA_sentence_to_entail(news_content.strip(), tweet.strip())
    if (only_qna_extract == None):
        only_qna_extract = "No Answer Available"
    only_similar_sent_summary = get_similar_sentences(news_content.strip(), tweet, similar_sentences_embedder, 3)
    if (only_similar_sent_summary == None):
        only_similar_sent_summary = "No Answer Available"
    headline_n_qna_extract = headline + " " + only_qna_extract
    headline_n_similar_summary = headline + " " + only_similar_sent_summary
    tokens = roberta.encode(headline, tweet)
    result_hl = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]

    tokens = roberta.encode(headline_n_newscontent, tweet)
    if (len(tokens) > 512):  tokens = tokens[0:511]
    result_hl_n_content = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]

    tokens = roberta.encode(only_qna_extract, tweet)
    if (len(tokens) > 512):  tokens = tokens[0:511]
    result_qna = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]

    tokens = roberta.encode(headline_n_qna_extract, tweet)
    if (len(tokens) > 512):  tokens = tokens[0:511]
    reslut_hl_n_qna = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]

    tokens = roberta.encode(only_similar_sent_summary, tweet)
    if (len(tokens) > 512):  tokens = tokens[0:511]
    result_simSents = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]

    tokens = roberta.encode(headline_n_similar_summary, tweet)
    if (len(tokens) > 512):  tokens = tokens[0:511]
    result_hl_n_simSents = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]

    return [result_hl, result_hl_n_content, result_qna, reslut_hl_n_qna, result_simSents, result_hl_n_simSents]


def remove_url_from_tweet(tweet_text):
    return re.sub(r"http\S+", "", tweet_text)


def remove_duplicates_in_df(input_df, column_name):
    output_df = input_df.drop_duplicates(subset=column_name, keep="first")


def get_data_from_df(df_name, some_number):
    row = df_name.iloc[some_number]
    return row["tweet"], row["scrapped text"], row["heading"]

def clean_data(text):
    if (text==None):
        text="Nothing"
    # data= re.sub('\s+', '', data)
    # data = re.sub('\n', ' ', data)
    # data = re.sub('\t', '', data)
    text = re.sub('&amp;', '', text)
    text = re.sub('& amp;', '', text)
    text = re.sub('#', '', text)
    # text = re.sub('[0-9]+', '', text)
    text  = "".join([char for char in text if char not in string.punctuation])

    return text

def entail_single_tweet_and_print(tweet_sentence):
    input_tweet = tweet_sentence
    print(
        "------------------ Doing a Google Search for relevant Articles..Hang ON -------------------------------------")
    input_tweet = clean_data(remove_url_from_tweet(input_tweet))
    url, title, content = content_extraction_from_tweet(input_tweet)

    count_hl = count_hl_content = count_qna = count_hl_qna = count_simsent = count_hl_simsent = combined_intelligence = 0
    total_articles_processed = 0
    start_time = time.time()
    for index in range(len(content)):
        tweet_hypothesis = input_tweet
        news_header_premise = clean_data(title[index]).strip()
        news_content_premise = clean_data(content[index]).strip()
        results = all_entaliments_at_once(tweet_hypothesis, news_content_premise, news_header_premise)
        result_hl = results[0]
        result_hl_n_content = results[1]
        result_qna = results[2]
        reslut_hl_n_qna = results[3]
        result_simSents = results[4]
        result_hl_n_simSents = results[5]
        if (result_hl == "contradiction"): count_hl += 1
        if (result_hl_n_content == "contradiction"): count_hl_content += 1
        if (result_qna == "contradiction"): count_qna += 1
        if (reslut_hl_n_qna == "contradiction"): count_hl_qna += 1
        if (result_simSents == "contradiction"): count_simsent += 1
        if (result_hl_n_simSents == "contradiction"): count_hl_simsent += 1

        if (result_qna == "contradiction" or
                reslut_hl_n_qna == "contradiction" or
                result_simSents == "contradiction" or
                result_hl_n_simSents == "contradiction"):
            combined_intelligence += 1
        total_articles_processed += 1
        print("The URL is :{}\n".format(url[index]))
        print("The Tweet is :\n{}\n".format(tweet_hypothesis))
        print(tabulate([[' Header only', result_hl],
                        ['Header + Content', result_hl_n_content],
                        ['Q&A Sentence only', result_qna],
                        ['Header + Q&A Sentence', reslut_hl_n_qna],
                        ['Similar Sentences only', result_simSents],
                        ['Header + Similar Sentences', result_hl_n_simSents],
                        ],
                       headers=['Tweet Entailed with', 'Result']))
        print("------------------------------------------------------")
    time_taken = (time.time() - start_time) / total_articles_processed

    print("Average Time for each entailment={:.4f} seconds".format(time_taken))
    print("Tweets entailment results are as follows:")
    print(tabulate([[' Header only', count_hl],
                    ['Header + Content', count_hl_content],
                    ['Q&A Sentence only', count_qna],
                    ['Header + Q&A Sentence', count_hl_qna],
                    ['Similar Sentences only', count_simsent],
                    ['Header + Similar Sentences', count_hl_simsent],
                    ['Combined Intelligence', combined_intelligence]

                    ],
                   headers=['Tweet Entailed with', 'Number of Contradictions']))
    print("------------------------------------------------------------------------------------")

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
        self.direct_claim = pickle.load(open(self.Dir_name+'classifier_module/direct_claim_classifier', 'rb'))
        self.indirect_claim = pickle.load(open(self.Dir_name+'classifier_module/indirect_claim_classifier', 'rb'))
        self.opinion = pickle.load(open(self.Dir_name+'classifier_module/opinion_classifier', 'rb'))
        self.quote = pickle.load(open(self.Dir_name+'classifier_module/quote_classifier', 'rb'))
        self.not_claim = pickle.load(open(self.Dir_name+'classifier_module/not_claim_classifier', 'rb'))
        self.level_2_classifier = pickle.load(open(self.Dir_name+'classifier_module/level_2_classifier', 'rb'))



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
        with open('classifier_module/classifiers_features.txt', 'r') as f:
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
    filename = './classifier_module/Test_svm.txt'
    classifier = Classifier()
    predict = classifier.prediction(filename)
    for each_tweet in predict:
        print(each_tweet)
        entail_single_tweet_and_print(each_tweet)


