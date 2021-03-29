import scipy
import spacy
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from sentence_transformers import SentenceTransformer
# for QA model-----------------------------------------
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
#for Roberta model--------------------------------------



# defs for similar sentence -----------------------------

def get_similar_sentences(paragraph,tweet,similar_sentences_embedder,closest_n=3):
    corpus=nltk.sent_tokenize(paragraph)
    corpus_embeddings = similar_sentences_embedder.encode(corpus)
    queries=nltk.sent_tokenize(tweet)
    query_embeddings = similar_sentences_embedder.encode(queries)
    for query, query_embedding in zip(queries, query_embeddings):
        distances = scipy.spatial.distance.cdist([query_embedding], corpus_embeddings, "cosine")[0]
        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1])
        similar_sents=[]
        for idx, distance in results[0:closest_n]:
            similar_sents.append(corpus[idx].strip())
        return similar_sents
#----------------------------------------------------------

# defs for Q& A based extraction-----------------------------

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
        # else:
        #     pass
# ----------------------------------------------------------------