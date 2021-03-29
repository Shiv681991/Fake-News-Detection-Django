'''
For demo
Input : 1 tweet
Procedure : Use google_search_api.py to obtain 10 urls and corresponding News contents
Use alBERT SQuAD Q&A to obtain sentence to entail
User BERT_Large to obtain sentence similarity summary
Need to check for headlines
get 6 entailment outputs and
Output : Check if it is entailed or not


'''
import sys
sys.path.append('/home/shivam/PycharmProjects/Django/Django_Warehouse/todo-django-rest-framework-master/todo_drf/api')
import pandas as pd
import csv
import torch
# from question_answering import QuestionAnsweringModel
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
                                "id": "Shivam_Sharma",
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

def get_QnA_sentence_to_entail(paragraph, tweet,unprocessed_content):
    dev_data = convert_qa_2_squad(paragraph, tweet)
    dev_data = [item for topic in dev_data['data'] for item in topic['paragraphs']]
    model_albert_large_v1 = QuestionAnsweringModel('albert',
                                                   './models/model_albert_large_v1_outputs', use_cuda=False)
    preds = model_albert_large_v1.predict(dev_data)
    print("preds: ",preds)
    albert_answer = preds[0]['answer']
    # albert_answer = preds[0][0]['answer'][0]
    corpus = nltk.sent_tokenize(paragraph)
    # corpus = nltk.sent_tokenize(unprocessed_content)
    print("corpus: ",corpus)
    # corpus=["Misinformation isn't going away just because it's a new year.", 'Support trusted, factual information with a tax deductible contribution to PolitiFact.', "Sen. Kamala Harris, D-Calif., joined the women's advocacy group, MomsRising, to protest against threats by President Donald Trump against Central American asylum-seekers to separate children from their parents at the U.S. Capitol in in May 2018.", '/ AP file\n California Democratic Sen. Kamala Harris has condemned President Donald Trump on numerous occasions.', 'Recently, she   Trump for not standing up to Russian President Vladimir Putin.', 'Not long ago, she   his administration’s handling of the aftermath of Hurricane Maria in Puerto Rico.', 'But Harris, who has been mentioned as a potential  , has saved some of her sharpest criticism for Trump’s policy that separated thousands of migrant families at the U.S.-Mexico border this spring.', '"Every single day these families are separated, another child goes to sleep terrified because they don’t know where their parents are," Harris   in a recent Facebook post.', '"All because of a policy used to punish immigrants fleeing violence.', 'This is not reflective of a civil society."', ', she wrote that "these children are in prison."', 'This week, Harris and two other Democratic senators introduced the   at the U.S. Capitol.', 'The bill would require the immediate reunification of families along with access to legal counsel and child advocates for those who have been separated.', 'She said the legislation is necessary to reunify the many children still separated.', '"Let’s talk about the facts and where we are today: There are still nearly 2,600 children who are separated from their parents," Harris said on July 17.', 'The separations stem from Trump’s "zero-tolerance" policy calling for the prosecution of all immigrants who illegally crossed into the United States at the southwest border.', 'Attorney General Jeff Sessions officially   April 6 as a deterrent to illegal immigration.', 'Trump signed an   family separations on June 20 after a backlash against that part of his policy.', 'We wanted to know, weeks after the Trump administration ended that policy, did Harris get her numbers right on how many children remain separated?', 'We set out on a fact check.', 'When asked for evidence, Harris’ spokesman pointed to testimony in a  \xa0from Chris Meekins, the deputy assistant secretary for preparedness and response at the U.S. Health and Human Services Department.', 'Meekins testified that 2,551 separated children ages five and up remained in the agency’s custody.', 'Politico   it was the first time the Trump administration had specified the exact number of separated children.', 'It added the "health department earlier had estimated only that ‘under 3,000 children’ were separated from their parents."', 'One week ago, HHS reported it had   under the age of five with their parents.', 'Adding those remaining young children, 46 as of last week, with the 2,551 children ages five and up, fits with Harris’ statement that "nearly 2,600" children remained separated as of mid-July.', 'The Trump administration said late last week it would speed up the reunification process.', 'But it’s not clear whether that’s resulted in a major change this week.', 'An HHS spokeswoman on July 19 said she could not immediately provide a current figure for the total number of children that remain separated.', 'on the agency’s website says HHS and other federal agencies are "working rapidly" to reunify eligible children with their parents under the orders of a U.S. District Court Judge Dana Sabraw of San Diego.', 'HHS is facing a July 26 court-ordered deadline to reunify all the children.', 'In a family reunification report issued this week, HHS said the 2,551 figure "represents the total possible 5-and-up cohort of minors who could be subject to the court order.', 'Based on past experience, it is likely to include a significant number of minors who are not eligible for reunification under the court’s order.', 'Not all of the 2,551 minors in HHS care will necessarily be reunified, because some adults claiming parentage may not actually be the parents or may be unfit or a danger to the children."', 'Sen. Kamala Harris claimed there "are still nearly 2,600 children who are separated from their parents," speaking on July 17.', 'A Trump administration official testified four days earlier that 2,551 children ages 5 and up remained separated.', 'That figure along with the 46 youngest children that the administration said remained separated as of mid July equates to "nearly 2,600."', 'A spokeswoman for the U.S. Health and Human Services Department could not provide a current total this week for the number of remaining separated children.', 'Still, Harris appears to have accurately described the total based on the publicly available information at the time of her statement.', 'We rate her claim True.', 'on the six PolitiFact ratings and how we select facts to check.', 'Sen. Kamala Harris, press conference and Facebook page, July 17, 2018 Tyrone Gayle, spokesman, Sen. Harris, email exchange July 18, 2018 Evelyn Stauffer, spokeswoman, U.S. Health and Human Services Department, email exchange July 19, 2018 United States District Court  , U.S. MS. L, et.', 'al., vs. U.S. Immigration and Customs Enforcement, et.', 'al., Declaration of Chris Meekins, July 13, 2018 U.S. Health and Human Services Department, press release,  , July 18, 2018 U.S. Health and Human Services Department,  , July 18, 2018 , July 13, 2018  Trump immigration policy, July 12, 2018 , July 12, 2018 \nIn a world of wild talk and fake news', 'help us stand up for the facts 1100 Connecticut Ave NW 801 3rd St S']
    for idx in range(len(corpus)):
        fullstring = corpus[idx]  # +corpus[idx+1]
        print("check: ",fullstring.find(albert_answer),fullstring)
        if fullstring.find(albert_answer)!=-1:
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


def all_entaliments_at_once(tweet, news_content, headline,unprocessed_content):
    #   get_QnA_sentence_to_entail(context,question)
    tweet = nltk.word_tokenize(tweet)
    print("------checking all answers--------")
    # print("tweet: ",tweet)
    news_content = nltk.word_tokenize(news_content)
    # print("news_content: ", news_content)
    headline = nltk.word_tokenize(headline)
    # print("headline: ", headline)
    headline_n_newscontent = headline + news_content
    headline_n_newscontent = " ".join(headline_n_newscontent).strip()
    # print("headline_n_newscontent : ", headline_n_newscontent )
    news_content = " ".join(news_content).strip()
    # print("news_content: ", news_content)
    headline = " ".join(headline).strip()
    # print("headline: ", headline)
    tweet = " ".join(tweet).strip()
    # print("tweet: ", tweet)
    # only_qna_extract = get_QnA_sentence_to_entail(news_content.strip(), tweet.strip(),unprocessed_content)
    # print("only_qna_extract: ", only_qna_extract)
    # if (only_qna_extract == None):
    #     only_qna_extract = "No Answer Available"
    only_similar_sent_summary = get_similar_sentences(news_content.strip(), tweet, similar_sentences_embedder, 3)
    # print("only_similar_sent_summary: ", only_similar_sent_summary)
    if (only_similar_sent_summary == None):
        only_similar_sent_summary = "No Answer Available"
    # headline_n_qna_extract = headline + " " + only_qna_extract
    # print("headline_n_qna_extract: ", headline_n_qna_extract)
    headline_n_similar_summary = headline + " " + only_similar_sent_summary
    # print("headline_n_similar_summary: ", headline_n_similar_summary)
    tokens = roberta.encode(headline, tweet)
    result_hl = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]

    tokens = roberta.encode(headline_n_newscontent, tweet)
    if (len(tokens) > 512):  tokens = tokens[0:511]
    result_hl_n_content = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]

    # tokens = roberta.encode(only_qna_extract, tweet)
    # if (len(tokens) > 512):  tokens = tokens[0:511]
    # result_qna = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]

    # tokens = roberta.encode(headline_n_qna_extract, tweet)
    # if (len(tokens) > 512):  tokens = tokens[0:511]
    # reslut_hl_n_qna = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]

    tokens = roberta.encode(only_similar_sent_summary, tweet)
    if (len(tokens) > 512):  tokens = tokens[0:511]
    result_simSents = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]
    probR = np.exp((roberta.predict('mnli', tokens)).detach().numpy())[0].tolist()

    tokens = roberta.encode(headline_n_similar_summary, tweet)
    if (len(tokens) > 512):  tokens = tokens[0:511]
    result_hl_n_simSents = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]

    # return [result_hl, result_hl_n_content, result_qna, reslut_hl_n_qna, result_simSents, result_hl_n_simSents]
    return [result_hl, result_hl_n_content, result_simSents, result_hl_n_simSents,probR]


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

def clean_data_not_punc(text):
    if (text==None):
        text="Nothing"
    # data= re.sub('\s+', '', data)
    # data = re.sub('\n', ' ', data)
    # data = re.sub('\t', '', data)
    text = re.sub('&amp;', '', text)
    text = re.sub('& amp;', '', text)
    text = re.sub('#', '', text)
    # text = re.sub('[0-9]+', '', text)
    # text  = "".join([char for char in text if char not in string.punctuation])

    return text

def start_entail(in_txt):
    print(
        "------------------ Doing a Google Search for relevant Articles..Hang ON -------------------------------------")
    input_tweet = clean_data(remove_url_from_tweet(in_txt))
    print("input tweet: ", input_tweet)
    url, title, content = content_extraction_from_tweet(input_tweet)
    # print("===========>{}".format(len(content)))
    # print("===========>{}".format(content))
    # print("url: ",url)
    # print("title: ", title)
    # print("content: ", content)
    count_hl = count_hl_content = count_qna = count_hl_qna = count_simsent = count_hl_simsent = combined_intelligence = 0
    total_articles_processed = 0
    start_time = time.time()
    out_dlist = []
    verd_list = []
    prob_list = []
    for index in range(len(content)):
        cur_prob=0
        # for index in range(1):
        tweet_hypothesis = input_tweet
        news_header_premise = clean_data(title[index]).strip()
        # print("unprocessed_content: ",content[index])
        # news_content_premise = clean_data(content[index]).strip()
        news_content_premise = clean_data_not_punc(content[index]).strip()
        if content[index] is not None:
            # print("content_check_none: ",content[index])
            # print("type check: ",type(content[index]))
            results = all_entaliments_at_once(tweet_hypothesis, news_content_premise, news_header_premise,
                                              content[index].strip())
            result_hl = results[0]
            result_hl_n_content = results[1]
            # result_qna = results[2]
            # reslut_hl_n_qna = results[3]
            # result_simSents = results[4]
            # result_hl_n_simSents = results[5]
            result_simSents = results[2]
            result_hl_n_simSents = results[3]
            prob_result_simSents = results[4]
            print("prob_result_simSents: ", prob_result_simSents)
            if (result_hl == "contradiction"): count_hl += 1
            if (result_hl_n_content == "contradiction"): count_hl_content += 1
            # if (result_qna == "contradiction"): count_qna += 1
            # if (reslut_hl_n_qna == "contradiction"): count_hl_qna += 1
            if (result_simSents == "contradiction"): count_simsent += 1
            if (result_hl_n_simSents == "contradiction"): count_hl_simsent += 1
            result_updated = result_simSents
            cur_output = 0
            cur_label = None
            if result_simSents == "neutral":
                new_list = set(prob_result_simSents)
                # removing the largest element from list1
                new_list.remove(max(new_list))
                # prob_result_simSents.index(max(new_list))
                result_updated = result_labels[prob_result_simSents.index(max(new_list))]
                if result_updated == "entailment":
                    cur_output = 0
                    verd_list.append(0)
                    cur_label = 'Not-Fake'
                else:
                    cur_output = 1
                    verd_list.append(1)
                    cur_label = 'Fake'
                cur_prob = max(new_list)
                prob_list.append(cur_prob)
                print(result_updated)
            else:
                cur_prob = max(set(prob_result_simSents))
                prob_list.append(cur_prob)
                if result_updated == "entailment":
                    cur_output = 0
                    verd_list.append(0)
                    cur_label = 'Not-Fake'
                else:
                    cur_output = 1
                    verd_list.append(1)
                    cur_label = 'Fake'
            # if (result_qna == "contradiction" or
            #         reslut_hl_n_qna == "contradiction" or
            #         result_simSents == "contradiction" or
            #         result_hl_n_simSents == "contradiction"):
            #     combined_intelligence += 1
            total_articles_processed += 1
            print(f"==============>Current verdict list: {verd_list}")
            out_dlist.append({'url': url[index], 'Result': cur_label, 'prob': np.round(cur_prob, 2)})
            print("The URL is :{}\n".format(url[index]))
            print("The Tweet is :\n{}\n".format(tweet_hypothesis))
            print("The prediction is: ", cur_output)
            # print(tabulate([[' Header only', result_hl],
            #                 ['Header + Content', result_hl_n_content],
            #                 ['Q&A Sentence only', result_qna],
            #                 ['Header + Q&A Sentence', reslut_hl_n_qna],
            #                 ['Similar Sentences only', result_simSents],
            #                 ['Header + Similar Sentences', result_hl_n_simSents],
            #                 ],
            #                headers=['Tweet Entailed with', 'Result']))
            print(tabulate([[' Header only', result_hl],
                            ['Header + Content', result_hl_n_content],
                            ['Similar Sentences only', result_simSents],
                            ['Header + Similar Sentences', result_hl_n_simSents],
                            ],
                           headers=['Tweet Entailed with', 'Result']))
            print(
                f"------------------------------------------------------end of {index + 1} url execution---------------------------------------------")
    print("number of articles: ", total_articles_processed)
    print("total time: ", (time.time() - start_time))
    try:
        time_taken = (time.time() - start_time) / (total_articles_processed)
    except:
        print("0 Articles processed. Kindly proceed!")
        return 0
    avg_prob = np.nanmean(prob_list)
    print("Average Time for each entailment={:.4f} seconds".format(time_taken))
    print(f"Verdict list: {verd_list}")
    final_verd_num = max(verd_list)
    if final_verd_num:
        final_verd = "Fake"
    else:
        final_verd = "Not-Fake"
    print("Final verdict:", final_verd)

    return {'Tweet': tweet_hypothesis, 'Result': final_verd, 'prob': np.round(avg_prob, 2), 'url_info': out_dlist}
    # print(tabulate([[' Header only', count_hl],
    #                 ['Header + Content',  count_hl_content],
    #                 ['Q&A Sentence only',  count_qna],
    #                 ['Header + Q&A Sentence',  count_hl_qna],
    #                 ['Similar Sentences only',  count_simsent],
    #                 ['Header + Similar Sentences',  count_hl_simsent],
    #                 ['Combined Intelligence',  combined_intelligence]
    #
    #                 ],
    #                headers=['Tweet Entailed with', 'Number of Contradictions']))


'''
        # print(url, title, content)
        # print()
        results1 = all_entaliments_at_once(input_tweet, clean_data(content[0]), clean_data(title[0]));print(results1)
        results2 = all_entaliments_at_once(input_tweet, clean_data(content[1]), clean_data(title[1]));print(results2)
        results3 = all_entaliments_at_once(input_tweet, clean_data(content[2]), clean_data(title[2]));print(results3)

'''



if __name__ == "__main__":
    while (1):
        input_tweet = input(" Please enter the tweet!!\n ")
        out_dct = start_entail(input_tweet)
        print(f"Output dictionary is: {out_dct}")
