# from models import entail_dl
import numpy as np
import pandas as pd
import sys
# import django
# django.setup()
# from django.apps import AppConfig
# from django.conf import settings
from tqdm import tqdm
# Push filtered tweets into the DB
# l1_list: list of lists of DB rows

# sys.exit()
from todo_drf.frontend.apps import FrontendAppConfig

from api.models import entail_jh as cur_db
# Task, Tweets, Tweets_L1, Tweets_L2, Tweets_L3, entaildata, fact_dli
# -----------------------------------------------
from tqdm import tqdm
f_name = 'Jharkhand'
in_file = '/home/shivam/PycharmProjects/Django/Django_Warehouse/todo-django-rest-framework-master/todo_drf/statewise_tweets/'+f_name+'_Tweets.csv'
cur_df = pd.read_csv(in_file)
# print(cur_df.head())
res_list, prob_list = FrontendAppConfig.text_FNF_classify(cur_df['text'].tolist())
cur_df['Verdict'] = res_list
cur_df['Prob'] = prob_list
# print(cur_df.head())
# print(cur_df.keys())
df_2 = cur_df[['description', 'Verdict', 'Prob']]
# print(df_2.head())
cur_list = df_2.values.tolist()
# print(np.shape(cur_list))


# cur_list.append()
# cur_list = []
cur_db.objects.all().delete()
# print("==========>Size of the L1 list", len(l1_list))
for ind, tweet_data in enumerate(cur_list):
    tweet_data = tweet_data + []
    t = cur_db(id = cur_df["Tweet_ID"].iloc[ind], tweet = tweet_data[0], res_cls = tweet_data[1], prob_cls = tweet_data[2], res_ent = tweet_data[1], prob_ent = tweet_data[2], iids = "Dummy Image ID",
                  u1 = "URL dummy", u1res = tweet_data[1], u1prob = tweet_data[2], u2 = "URL dummy", u2res = tweet_data[1], u2prob = tweet_data[2],
                  u3 = "URL dummy", u3res = tweet_data[1], u3prob = tweet_data[2], u4 = "URL dummy", u4res = tweet_data[1], u4prob = tweet_data[2],
                  u5 = "URL dummy", u5res = tweet_data[1], u5prob = tweet_data[2], u6 = "URL dummy", u6res = tweet_data[1], u6prob = tweet_data[2],
                  u7 = "URL dummy", u7res = tweet_data[1], u7prob = tweet_data[2], u8 = "URL dummy", u8res = tweet_data[1], u8prob = tweet_data[2],
                  u9 = "URL dummy", u9res = tweet_data[1], u9prob = tweet_data[2], u10 = "URL dummy", u10res = tweet_data[1], u10prob = tweet_data[2])
    t.save()
print("===========>DB populated!")
# -----------------------------------------------