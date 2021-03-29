from django.apps import AppConfig
from .demo_Fakenews_test14mar21 import start_entail
# roberta = torch.hub.load('pytorch/fairseq', 'roberta.large.mnli')
# roberta.eval()  # disable dropout for evaluation
# result_labels = ["contradiction", "neutral", "entailment"]

# # =======================================================
# # Before Delegation
# # =======================================================
# # Entailment functions and code
# # Utility modules/defs
# def convert_qa_2_squad(paragraph, question):
#     dev_data = {
#         "version": "v2.0",
#         "data": [
#             {
#                 "title": "TestQuestion",
#                 "paragraphs": [
#                     {
#                         "qas": [
#                             {
#                                 "question": "Any Question?",
#                                 "id": "Bob_Chait",
#                                 "answers": [
#                                     {
#                                         "text": "Any_answer is Fine",
#                                         "answer_start": 170
#                                     }
#                                 ],
#                                 "is_impossible": False
#                             }
#                         ],
#                         "context": "Any Paragraph here"
#                     }
#                 ]
#             }
#         ]
#     }
#     for datum in dev_data["data"]:
#         for para in datum["paragraphs"]:
#             # print(para["context"])
#             para["context"] = paragraph
#             for qa in para["qas"]:
#                 qa["question"] = question
#     with open('result.json', 'w') as fp:
#         json.dump(dev_data, fp)
#     return dev_data
#
# def get_QnA_sentence_to_entail(paragraph, tweet):
#     dev_data = convert_qa_2_squad(paragraph, tweet)
#     dev_data = [item for topic in dev_data['data'] for item in topic['paragraphs']]
#     model_albert_large_v1 = QuestionAnsweringModel('albert',
#                                                    os.path.join(settings.MODELS, 'model_albert_large_v1_outputs'), use_cuda=False)
#     preds = model_albert_large_v1.predict(dev_data)
#     albert_answer = preds[0][0]['answer'][0]
#     corpus = nltk.sent_tokenize(paragraph)
#     for idx in range(len(corpus)):
#         fullstring = corpus[idx]  # +corpus[idx+1]
#         if fullstring.find(albert_answer):
#             return fullstring
#         else:
#             pass
#
#
# similar_sentences_embedder = SentenceTransformer('bert-base-nli-mean-tokens')
#
#
# def get_similar_sentences(paragraph, tweet, similar_sentences_embedder, closest_n=3):
#     corpus = nltk.sent_tokenize(paragraph)
#     corpus_embeddings = similar_sentences_embedder.encode(corpus)
#     queries = nltk.sent_tokenize(tweet)
#     query_embeddings = similar_sentences_embedder.encode(queries)
#     for query, query_embedding in zip(queries, query_embeddings):
#         distances = scipy.spatial.distance.cdist([query_embedding], corpus_embeddings, "cosine")[0]
#         results = zip(range(len(distances)), distances)
#         results = sorted(results, key=lambda x: x[1])
#         similar_sents = []
#         for idx, distance in results[0:closest_n]:
#             similar_sents.append(corpus[idx].strip())
#         return (" ".join(similar_sents))
#
#
# def all_entaliments_at_once(tweet, news_content, headline):
#     #   get_QnA_sentence_to_entail(context,question)
#     tweet = nltk.word_tokenize(tweet)
#     news_content = nltk.word_tokenize(news_content)
#     headline = nltk.word_tokenize(headline)
#     headline_n_newscontent = headline + news_content
#     headline_n_newscontent = " ".join(headline_n_newscontent).strip()
#     news_content = " ".join(news_content).strip()
#     headline = " ".join(headline).strip()
#     tweet = " ".join(tweet).strip()
#     only_qna_extract = get_QnA_sentence_to_entail(news_content.strip(), tweet.strip())
#     if (only_qna_extract == None):
#         only_qna_extract = "No Answer Available"
#     only_similar_sent_summary = get_similar_sentences(news_content.strip(), tweet, similar_sentences_embedder, 3)
#     if (only_similar_sent_summary == None):
#         only_similar_sent_summary = "No Answer Available"
#     headline_n_qna_extract = headline + " " + only_qna_extract
#     headline_n_similar_summary = headline + " " + only_similar_sent_summary
#     tokens = roberta.encode(headline, tweet)
#     if (len(tokens) > 512):  tokens = tokens[0:511]
#     result_hl_prob = math.exp(np.max(roberta.predict('mnli', tokens).cpu().detach().numpy()))
#     result_hl = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]
#
#     tokens = roberta.encode(headline_n_newscontent, tweet)
#     if (len(tokens) > 512):  tokens = tokens[0:511]
#     result_hl_n_content_prob = math.exp(np.max(roberta.predict('mnli', tokens).cpu().detach().numpy()))
#     result_hl_n_content = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]
#
#     tokens = roberta.encode(only_qna_extract, tweet)
#     if (len(tokens) > 512):  tokens = tokens[0:511]
#     result_qna_prob = math.exp(np.max(roberta.predict('mnli', tokens).cpu().detach().numpy()))
#     result_qna = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]
#
#     tokens = roberta.encode(headline_n_qna_extract, tweet)
#     if (len(tokens) > 512):  tokens = tokens[0:511]
#     result_hl_n_qna_prob = math.exp(np.max(roberta.predict('mnli', tokens).cpu().detach().numpy()))
#     result_hl_n_qna = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]
#
#     tokens = roberta.encode(only_similar_sent_summary, tweet)
#     if (len(tokens) > 512):  tokens = tokens[0:511]
#     result_simSents_prob = math.exp(np.max(roberta.predict('mnli', tokens).cpu().detach().numpy()))
#     result_simSents = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]
#
#     tokens = roberta.encode(headline_n_similar_summary, tweet)
#     if (len(tokens) > 512):  tokens = tokens[0:511]
#     result_hl_n_simSents_prob = math.exp(np.max(roberta.predict('mnli', tokens).cpu().detach().numpy()))
#     result_hl_n_simSents = result_labels[(roberta.predict('mnli', tokens).argmax()).cpu().detach().numpy()]
#
#     return [result_hl, result_hl_prob, result_hl_n_content, result_hl_n_content_prob, result_qna, result_qna_prob, result_hl_n_qna, result_hl_n_qna_prob, result_simSents, result_simSents_prob, result_hl_n_simSents, result_hl_n_simSents_prob]
#
#
# def remove_url_from_tweet(tweet_text):
#     # print("=================>Tweet Text b4 RE{}".format(tweet_text))
#     return re.sub(r"http\S+", "", tweet_text)
#
#
# def remove_duplicates_in_df(input_df, column_name):
#     output_df = input_df.drop_duplicates(subset=column_name, keep="first")
#
#
# def get_data_from_df(df_name, some_number):
#     row = df_name.iloc[some_number]
#     return row["tweet"], row["scrapped text"], row["heading"]
#
# def clean_data(text):
#     if (text==None):
#         text="Nothing"
#     # data= re.sub('\s+', '', data)
#     # data = re.sub('\n', ' ', data)
#     # data = re.sub('\t', '', data)
#     text = re.sub('&amp;', '', text)
#     text = re.sub('& amp;', '', text)
#     text = re.sub('#', '', text)
#     # text = re.sub('[0-9]+', '', text)
#     text  = "".join([char for char in text if char not in string.punctuation])
#
#     return text
# # =======================================================
#
#
#
#
# # =======================================================
# # =======================================================
# # L1-L3 classification functions and code
# stop_words = set(stopwords.words('english'))
#
# def punctuations(string):
#     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     string = string.split()
#     string1 = []
#     for x in string:
#         if x not in punctuations:
#             if x.isalnum() == True:
#                 string1.append(x)
#     string = ' '.join(string1)
#     return string
#
# def remove_stopwords(line):
#     line = line.split()
#     tweet = []
#     for word in line:
#         if word not in stop_words:
#             tweet.append(word)
#     return ' '.join(tweet)
#
# def ngrams(tweet):
#     tweetsenco = []
#     words = tweet.split()
#     for i in range(2):
#         for j in range(len(words) - (i + 1)):
#             tweetsenco.append(' '.join(words[j:j + i + 2]))
#     return tweetsenco
# # =======================================================
class ApiConfig(AppConfig):
    name = 'api'
class PredictorConfig(AppConfig):
    # # ===============================================
    # # FACTDEMIC phase 1 classification code begins
    # # ===============================================
    # features = []
    # with open(os.path.join(settings.MODELS, 'classifiers_features.txt'), 'r') as f:
    #     for line in f:
    #         line = line.strip()
    #         features.append(line)
    #
    # direct_claim = pickle.load(open(os.path.join(settings.MODELS, 'direct_claim_classifier'), 'rb'))
    # direct_claim_probs = pickle.load(open(os.path.join(settings.MODELS, 'direct_claim_classifier_proba'), 'rb'))
    # indirect_claim = pickle.load(open(os.path.join(settings.MODELS, 'indirect_claim_classifier'), 'rb'))
    # indirect_claim_probs = pickle.load(open(os.path.join(settings.MODELS, 'indirect_claim_classifier_proba'), 'rb'))
    # opinion = pickle.load(open(os.path.join(settings.MODELS, 'opinion_classifier'), 'rb'))
    # opinion_probs = pickle.load(open(os.path.join(settings.MODELS, 'opinion_classifier_proba'), 'rb'))
    # quote = pickle.load(open(os.path.join(settings.MODELS, 'quote_classifier'), 'rb'))
    # quote_probs = pickle.load(open(os.path.join(settings.MODELS, 'quote_classifier_proba'), 'rb'))
    # not_claim = pickle.load(open(os.path.join(settings.MODELS, 'not_claim_classifier'), 'rb'))
    # not_claim_probs = pickle.load(open(os.path.join(settings.MODELS, 'not_claim_classifier_proba'), 'rb'))
    # level_2_classifier = pickle.load(open(os.path.join(settings.MODELS, 'level_2_classifier'), 'rb'))
    # level_2_classifier_probs = pickle.load(open(os.path.join(settings.MODELS, 'level_2_classifier_proba'), 'rb'))
    # level_3_classifier = pickle.load(open(os.path.join(settings.MODELS, 'level_3_classifier'), 'rb'))
    #
    # def pre_processing(text):
    #     text = ' '.join(twokenizer.tokenizeRawTweetText(text))
    #     text = punctuations(text)
    #     text = remove_stopwords(text)
    #     ngram = ngrams(text)
    #     return ngram
    #
    # multi_hot = MultiLabelBinarizer(classes=features)
    #
    #
    # # Initializing the vectors and labels for l3 classifier
    #
    # x = [[0, 0, 0, 0, 0, 0, 0, 1, 0],
    #      [1, 0, 0, 0, 0, 0, 0, 0, 0],
    #      [0, 1, 0, 0, 0, 0, 0, 0, 0],
    #      [0, 0, 0, 0, 0, 0, 1, 0, 0],
    #      [0, 0, 0, 1, 0, 0, 0, 0, 0],
    #      [0, 0, 1, 0, 0, 0, 0, 0, 0],
    #      [0, 0, 0, 0, 1, 0, 0, 0, 0],
    #      [0, 0, 0, 0, 0, 1, 0, 0, 0],
    #      [0, 0, 0, 0, 0, 0, 0, 0, 1],
    #      [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    # y = ['rumors',
    #      'authorities',
    #      'fake_cure',
    #      'religious',
    #      'panic',
    #      'others',
    #      'political',
    #      'racist',
    #      'xenophobic',
    #      'others']
    #
    #
    # iids_demo = []
    # tweets_demo = []
    # tweets_raw_demo = []
    #
    # iids_city = []
    # tweets_city = []
    # tweets_raw_city = []
    # # 'caps_100.txt'
    # # Tweets_Delhi
    # filename1 = os.path.join(settings.MODELS, 'Tweet_Files/Raw_IIDTweets/sample_tweets_proc.csv')
    # filename2 = os.path.join(settings.MODELS, 'Tweet_Files/Raw_IIDTweets/Tweets_Delhi.csv')
    #
    # with open(filename1, 'r') as f1:
    #     for ind, line in enumerate(f1):
    #         if len(line)<2:
    #             continue
    #         iid_demo, tweet_demo = line.split(',')[0], ','.join(line.split(',')[1:])
    #         tweets_demo.append(tweet_demo.strip().lower())
    #         tweets_raw_demo.append(tweet_demo.strip())
    #         iids_demo.append(iid_demo)
    #         # print("===========>Prining pout JPGS")
    #         # print(iid)
    # with open(filename2, 'r') as f2:
    #     for ind, line in enumerate(f2):
    #         if len(line)<2:
    #             continue
    #         iid_city, tweet_city = line.split(',')[0], ','.join(line.split(',')[1:])
    #         tweets_city.append(tweet_city.strip().lower())
    #         tweets_raw_city.append(tweet_city.strip())
    #         iids_city.append(iid_city)
    #         # print("===========>Prining pout JPGS")
    #         # print(iid)
    #
    # # sys.exit()
    # feature = ['tweets', 'direct_claim', 'direct_claim_probability', 'indirect_claim', 'indirect_claim_probability',
    #            'opinion', 'opinion_probability', 'quote', 'quote_probability', 'not_claim', 'not_claim_probability',
    #            'level_2', 'level_2_probability', 'level_3_tag', 'iids']
    # data_demo = pd.DataFrame(columns=feature)
    # data_demo['tweets'] = tweets_demo
    # data_demo['iids'] = iids_demo
    # data_city = pd.DataFrame(columns=feature)
    # data_city['tweets'] = tweets_city
    # data_city['iids'] = iids_city
    # # print(len(tweets), len(iids))
    # # print(data['iids'])
    #
    # contexts_demo = []
    # for i in data_demo['tweets']:
    #     ngram = pre_processing(i)
    #     context_demo = []
    #     for k in ngram:
    #         if k in features:
    #             context_demo.append(k)
    #     contexts_demo.append(context_demo)
    # data_demo['tweets_ngrams'] = contexts_demo
    #
    # contexts_city = []
    # for i in data_city['tweets']:
    #     ngram = pre_processing(i)
    #     context_city = []
    #     for k in ngram:
    #         if k in features:
    #             context_city.append(k)
    #     contexts_city.append(context_city)
    # data_city['tweets_ngrams'] = contexts_city
    #
    # encoded_text_demo = multi_hot.fit_transform(contexts_demo)
    # encoded_text_city = multi_hot.fit_transform(contexts_city)
    #
    # for i in range(len(encoded_text_demo)):
    #     result_demo = direct_claim.predict([encoded_text_demo[i]])
    #     result_prob_demo = max(direct_claim_probs.predict_proba([encoded_text_demo[i]]))
    #     if result_demo == [0]:
    #         data_demo['direct_claim'][i] = 'yes'
    #         data_demo['direct_claim_probability'][i] = max(result_prob_demo)
    #     else:
    #         data_demo['direct_claim'][i] = 'no'
    #         data_demo['direct_claim_probability'][i] = max(result_prob_demo)
    #     result_demo = indirect_claim.predict([encoded_text_demo[i]])
    #     result_prob_demo = max(indirect_claim_probs.predict_proba([encoded_text_demo[i]]))
    #     if result_demo == [0]:
    #         data_demo['indirect_claim'][i] = 'yes'
    #         data_demo['indirect_claim_probability'][i] = max(result_prob_demo)
    #     else:
    #         data_demo['indirect_claim'][i] = 'no'
    #         data_demo['indirect_claim_probability'][i] = max(result_prob_demo)
    #     result_demo = not_claim.predict([encoded_text_demo[i]])
    #     result_prob_demo = max(not_claim_probs.predict_proba([encoded_text_demo[i]]))
    #     if result_demo == [0]:
    #         data_demo['not_claim'][i] = 'yes'
    #         data_demo['not_claim_probability'][i] = max(result_prob_demo)
    #     else:
    #         data_demo['not_claim'][i] = 'no'
    #         data_demo['not_claim_probability'][i] = max(result_prob_demo)
    #     result_demo = opinion.predict([encoded_text_demo[i]])
    #     result_prob_demo = max(opinion_probs.predict_proba([encoded_text_demo[i]]))
    #     if result_demo == [0]:
    #         data_demo['opinion'][i] = 'yes'
    #         data_demo['opinion_probability'][i] = max(result_prob_demo)
    #     else:
    #         data_demo['opinion'][i] = 'no'
    #         data_demo['opinion_probability'][i] = max(result_prob_demo)
    #     result_demo = quote.predict([encoded_text_demo[i]])
    #     result_prob_demo = max(quote_probs.predict_proba([encoded_text_demo[i]]))
    #     if result_demo == [1]:
    #         data_demo['quote'][i] = 'yes'
    #         data_demo['quote_probability'][i] = max(result_prob_demo)
    #     else:
    #         data_demo['quote'][i] = 'no'
    #         data_demo['quote_probability'][i] = max(result_prob_demo)
    #
    #
    # for i in range(len(encoded_text_city)):
    #     result_city = direct_claim.predict([encoded_text_city[i]])
    #     result_prob_city = max(direct_claim_probs.predict_proba([encoded_text_city[i]]))
    #     if result_city == [0]:
    #         data_city['direct_claim'][i] = 'yes'
    #         data_city['direct_claim_probability'][i] = max(result_prob_city)
    #     else:
    #         data_city['direct_claim'][i] = 'no'
    #         data_city['direct_claim_probability'][i] = max(result_prob_city)
    #     result_city = indirect_claim.predict([encoded_text_city[i]])
    #     result_prob_city = max(indirect_claim_probs.predict_proba([encoded_text_city[i]]))
    #     if result_city == [0]:
    #         data_city['indirect_claim'][i] = 'yes'
    #         data_city['indirect_claim_probability'][i] = max(result_prob_city)
    #     else:
    #         data_city['indirect_claim'][i] = 'no'
    #         data_city['indirect_claim_probability'][i] = max(result_prob_city)
    #     result_city = not_claim.predict([encoded_text_city[i]])
    #     result_prob_city = max(not_claim_probs.predict_proba([encoded_text_city[i]]))
    #     if result_city == [0]:
    #         data_city['not_claim'][i] = 'yes'
    #         data_city['not_claim_probability'][i] = max(result_prob_city)
    #     else:
    #         data_city['not_claim'][i] = 'no'
    #         data_city['not_claim_probability'][i] = max(result_prob_city)
    #     result_city = opinion.predict([encoded_text_city[i]])
    #     result_prob_city = max(opinion_probs.predict_proba([encoded_text_city[i]]))
    #     if result_city == [0]:
    #         data_city['opinion'][i] = 'yes'
    #         data_city['opinion_probability'][i] = max(result_prob_city)
    #     else:
    #         data_city['opinion'][i] = 'no'
    #         data_city['opinion_probability'][i] = max(result_prob_city)
    #     result_city = quote.predict([encoded_text_city[i]])
    #     result_prob_city = max(quote_probs.predict_proba([encoded_text_city[i]]))
    #     if result_city == [1]:
    #         data_city['quote'][i] = 'yes'
    #         data_city['quote_probability'][i] = max(result_prob_city)
    #     else:
    #         data_city['quote'][i] = 'no'
    #         data_city['quote_probability'][i] = max(result_prob_city)
    #
    #
    # # Push Conditioned data into the L1 DB - using the following format for all the attributes
    # # ['tweets','direct_claim','indirect_claim','opinion','quote','not_claim','level_2','tweets_ngrams']
    # # data_l1 = data[(data['direct_claim'] == 'yes') | (data['indirect_claim'] == 'yes') | (data['opinion'] == 'yes') | (data['quote'] == 'yes')]
    # data_l1_demo = data_demo[data_demo['not_claim'] != 'yes']
    # data_l1_list_demo = data_l1_demo.values.tolist()
    # data_l1_city = data_city[data_city['not_claim'] != 'yes']
    # data_l1_list_city = data_l1_city.values.tolist()
    # # print("data_l1_list")
    # # print(data_l1_list[0])
    #
    # contexts_demo = data_demo['tweets_ngrams']
    # encoded_text_demo = multi_hot.fit_transform(contexts_demo)
    # contexts_city = data_city['tweets_ngrams']
    # encoded_text_city = multi_hot.fit_transform(contexts_city)
    # for i in range(len(encoded_text_demo)):
    #     result_demo = level_2_classifier.predict([encoded_text_demo[i]])
    #     result_level_2_prob_demo = max(level_2_classifier_probs.predict_proba([encoded_text_demo[i]]))
    #     if result_demo == [0]:
    #         data_demo['level_2'][i] = 'fact_check'
    #         data_demo['level_2_probability'][i] = max(result_level_2_prob_demo)
    #     elif result_demo == [1]:
    #         data_demo['level_2'][i] = 'pass'
    #         data_demo['level_2_probability'][i] = result_level_2_prob_demo
    #
    # for i in range(len(encoded_text_city)):
    #     result_city = level_2_classifier.predict([encoded_text_city[i]])
    #     result_level_2_prob_city = max(level_2_classifier_probs.predict_proba([encoded_text_city[i]]))
    #     if result_city == [0]:
    #         data_city['level_2'][i] = 'fact_check'
    #         data_city['level_2_probability'][i] = max(result_level_2_prob_city)
    #     elif result_city == [1]:
    #         data_city['level_2'][i] = 'pass'
    #         data_city['level_2_probability'][i] = result_prob_city
    #
    # data_l2_demo = data_demo[data_demo['level_2'] == 'fact_check']
    # data_l2_list_demo = data_l2_demo.values.tolist()
    # data_l2_city = data_city[data_city['level_2'] == 'fact_check']
    # data_l2_list_city = data_l2_city.values.tolist()
    # # print("data_l2_list")
    # # print(data_l2_list[0])
    #
    # contexts_demo = data_demo['tweets_ngrams']
    # encoded_text_demo = multi_hot.fit_transform(contexts_demo)
    # contexts_city = data_city['tweets_ngrams']
    # encoded_text_city = multi_hot.fit_transform(contexts_city)
    # for i in range(len(encoded_text_demo)):
    #     result_demo = level_3_classifier.predict([encoded_text_demo[i]])
    #     result_demo = result_demo.tolist()
    #     if result_demo[0] in x:
    #         tag_demo = y[x.index(result_demo[0])]
    #         data_demo['level_3_tag'][i] = tag_demo
    # for i in range(len(encoded_text_city)):
    #     result_city = level_3_classifier.predict([encoded_text_city[i]])
    #     result_city = result_city.tolist()
    #     if result_city[0] in x:
    #         tag_city = y[x.index(result_city[0])]
    #         data_city['level_3_tag'][i] = tag_city
    #
    # # No. of category wise tweets from L3
    # rumors_data_demo = len(data_demo[data_demo['level_3_tag'] == 'rumors'])
    # authorities_data_demo = len(data_demo[data_demo['level_3_tag'] == 'authorities'])
    # fake_cure_data_demo = len(data_demo[data_demo['level_3_tag'] == 'fake_cure'])
    # religious_data_demo = len(data_demo[data_demo['level_3_tag'] == 'religious'])
    # panic_data_demo = len(data_demo[data_demo['level_3_tag'] == 'panic'])
    # others_data1_demo = len(data_demo[data_demo['level_3_tag'] == 'others'])
    # political_data_demo = len(data_demo[data_demo['level_3_tag'] == 'political'])
    # racist_data_demo = len(data_demo[data_demo['level_3_tag'] == 'racist'])
    # xenophobic_data_demo = len(data_demo[data_demo['level_3_tag'] == 'xenophobic'])
    # others_data2_demo = len(data_demo[data_demo['level_3_tag'] == 'others'])
    #
    # # No. of category wise tweets from L3
    # rumors_data_city = len(data_city[data_city['level_3_tag'] == 'rumors'])
    # authorities_data_city = len(data_city[data_city['level_3_tag'] == 'authorities'])
    # fake_cure_data_city = len(data_city[data_city['level_3_tag'] == 'fake_cure'])
    # religious_data_city = len(data_city[data_city['level_3_tag'] == 'religious'])
    # panic_data_city = len(data_city[data_city['level_3_tag'] == 'panic'])
    # others_data1_city = len(data_city[data_city['level_3_tag'] == 'others'])
    # political_data_city = len(data_city[data_city['level_3_tag'] == 'political'])
    # racist_data_city = len(data_city[data_city['level_3_tag'] == 'racist'])
    # xenophobic_data_city = len(data_city[data_city['level_3_tag'] == 'xenophobic'])
    # others_data2_city = len(data_city[data_city['level_3_tag'] == 'others'])
    # # print("Final stats")
    # final_stat_demo = [rumors_data_demo, authorities_data_demo, fake_cure_data_demo,
    #       religious_data_demo, panic_data_demo, others_data1_demo, political_data_demo,
    #       racist_data_demo, xenophobic_data_demo, others_data2_demo]
    # # print("Final stats")
    # final_stat_city = [rumors_data_city, authorities_data_city, fake_cure_data_city,
    #                    religious_data_city, panic_data_city, others_data1_city, political_data_city,
    #                    racist_data_city, xenophobic_data_city, others_data2_city]
    # # print(final_stat)
    # data_l3_demo = data_demo[(data_demo['level_2'] == 'fact_check') | (data_demo['not_claim'] != 'yes')]
    # data_l3_list_demo = data_l3_demo.values.tolist()
    # data_l3_city = data_city[(data_city['level_2'] == 'fact_check') | (data_city['not_claim'] != 'yes')]
    # data_l3_list_city = data_l3_city.values.tolist()
    # # print("data_l3_list")
    # # print(data_l3_list[0])
    # # print("=============>L3 city list")
    # # print(data_l3_list_city)
    # # sys.exit()
    # # ===============================================
    # # FACTDEMIC phase 1 classification code ends
    # # ===============================================

    # Process for the entailment part using "data_l2_list" and entailment code

    # data_l3_list_proc = data_l3_list_demo
    # for ind, tweet in enumerate(data_l3_list_proc):
    def fake_verdict(tweet):
        tmp_res_dct = start_entail(tweet)
        return tmp_res_dct
        # # -------------------------------------
        # # Previous entailment code begins
        # # -------------------------------------
        # # ent_list = []
        # input_tweet = tweet
        # # cur_id = tweet[14]
        # # if len(input_tweet.split())>20:
        # #     continue
        # #     # input_tweet = ' '.join(input_tweet.split()[:20])
        # # print("------------------Tweet No. {} Doing a Google Search for relevant Articles..Hang ON -------------------------------------".format(ind))
        # print("------------------Tweet No. {} Doing a Google Search for relevant Articles..Hang ON -------------------------------------")
        # input_tweet = clean_data(remove_url_from_tweet(input_tweet))
        # url, title, content = content_extraction_from_tweet(input_tweet)
        # # print("===========>{}".format(len(content)))
        # # print("===========>{}".format(content))
        # count_hl = count_hl_content = count_qna = count_hl_qna = count_simsent = count_hl_simsent = combined_intelligence = 0
        # total_articles_processed = 0
        # start_time = time.time()
        # tweet_prob=[]
        # # N = len(content)
        # N = 1
        # for index in range(N):
        #     tweet_hypothesis = input_tweet
        #     news_header_premise = clean_data(title[index]).strip()
        #     news_content_premise = clean_data(content[index]).strip()
        #     results = all_entaliments_at_once(tweet_hypothesis, news_content_premise, news_header_premise)
        #     result_hl = results[0]
        #     result_hl_prob = results[1]
        #     result_hl_n_content = results[2]
        #     result_hl_n_content_prob = results[3]
        #     result_qna = results[4]
        #     result_qna_prob = results[5]
        #     result_hl_n_qna = results[6]
        #     result_hl_n_qna_prob = results[7]
        #     result_simSents = results[8]
        #     result_simSents_prob = results[9]
        #     result_hl_n_simSents = results[10]
        #     result_hl_n_simSents_prob = results[11]
        #     if (result_hl == "contradiction"): count_hl += 1
        #     if (result_hl_n_content == "contradiction"): count_hl_content += 1
        #     if (result_qna == "contradiction"): count_qna += 1
        #     if (result_hl_n_qna == "contradiction"): count_hl_qna += 1
        #     if (result_simSents == "contradiction"): count_simsent += 1
        #     if (result_hl_n_simSents == "contradiction"): count_hl_simsent += 1
        #
        #     if (result_qna == "contradiction" or
        #             result_hl_n_qna == "contradiction" or
        #             result_simSents == "contradiction" or
        #             result_hl_n_simSents == "contradiction"):
        #         combined_intelligence += 1
        #     choice_list = [result_qna, result_hl_n_qna, result_simSents, result_hl_n_simSents]
        #     # print("=======choice_list", choice_list)
        #     prob_list = [result_qna_prob,result_hl_n_qna_prob,result_simSents_prob,result_hl_n_simSents_prob]
        #     # print("=======prob_list", prob_list)
        #     choice_flag_list = [1 if elem=='contradiction' else 0 for elem in choice_list]
        #     # print("=======choice_flag_list", choice_flag_list)
        #     combined_intelligence_prob = np.dot(prob_list, choice_flag_list)/np.sum(choice_flag_list)
        #     # print("=======combined_intelligence_prob", combined_intelligence_prob)
        #     tweet_prob.append(combined_intelligence_prob)
        #     print("=====>CI Prob for index {}: {}".format(index, combined_intelligence_prob))
        #     total_articles_processed += 1
        #     print("The URL is :{}\n".format(url[index]))
        #     print("The Tweet is :\n{}\n".format(tweet_hypothesis))
        #     print(tabulate([[' Header only', result_hl],
        #                     ['Header + Content', result_hl_n_content],
        #                     ['Q&A Sentence only', result_qna],
        #                     ['Header + Q&A Sentence', result_hl_n_qna],
        #                     ['Similar Sentences only', result_simSents],
        #                     ['Header + Similar Sentences', result_hl_n_simSents],
        #                     ],
        #                    headers=['Tweet Entailed with', 'Result']))
        #     print("------------------------------------------------------")
        # time_taken = (time.time() - start_time) / total_articles_processed
        #
        # print("Average Time for each entailment={:.4f} seconds".format(time_taken))
        # print("Tweets entailment results are as follows:")
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
        # # cur_ent_con = [input_tweet, result_hl, result_hl_n_content, result_qna, result_hl_n_qna, result_simSents, result_hl_n_simSents, count_hl, count_hl_content, count_qna, count_hl_qna, count_simsent, count_hl_simsent, combined_intelligence]
        # if combined_intelligence>5:
        #     FNF = "fake"
        # else:
        #     FNF = "real"
        # # To be calculated dynamically
        # cleaned_prob_list = [x for x in tweet_prob if str(x) != 'nan']
        # prob = round(np.mean(cleaned_prob_list),2)
        # if prob=='nan':
        #     prob=0
        # print("===========Top Prob")
        # print(prob)
        # url_con = []
        # print('Tweet probability: ', tweet_prob)
        # for ind, u in enumerate(url[:N]):
        #     url_con.append(', '.join([u, str(round(tweet_prob[ind],2))]))
        #     print(url_con)
        # cur_ent_con = [input_tweet, FNF, prob] + url_con
        # print(cur_ent_con)
        # # ent_list.append(cur_ent_con)
        # # print(cur_ent_con)
        # return cur_ent_con[1:]
        # # t = entaildata(tweet=cur_ent_con[0], FNF=cur_ent_con[1], prob=cur_ent_con[2], u1=cur_ent_con[3], u2=cur_ent_con[4],
        # #                u3=cur_ent_con[5], u4=cur_ent_con[6], u5=cur_ent_con[7], u6=cur_ent_con[8], u7=cur_ent_con[9],
        # #                u8=cur_ent_con[10], u9=cur_ent_con[11], u10=cur_ent_con[12])
        # # t.save()
        # # -------------------------------------
        # # Previous entailment code ends
        # # -------------------------------------



