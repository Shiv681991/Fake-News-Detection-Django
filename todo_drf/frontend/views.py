from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import locationForm, UploadFileForm, in_textForm, stateForm
from .apps import FrontendAppConfig
import sys
sys.path.append("/home/shivam/PycharmProjects/Django/Django_Warehouse/todo-django-rest-framework-master/todo_drf")
from api.apps import PredictorConfig
import urllib
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import random
import dateutil
from twython import Twython

# from api.models import entail_jh as cur_db
# # Task, Tweets, Tweets_L1, Tweets_L2, Tweets_L3, entaildata, fact_dli
# # -----------------------------------------------
# from tqdm import tqdm
# f_name = 'Jharkhand'
# in_file = 'path_to_statewise_tweets/'+f_name+'_Tweets.csv'
# cur_df = pd.read_csv(in_file)
# # print(cur_df.head())
# res_list, prob_list = FrontendAppConfig.text_FNF_classify(cur_df['text'].tolist())
# cur_df['Verdict'] = res_list
# cur_df['Prob'] = prob_list
# # print(cur_df.head())
# # print(cur_df.keys())
# df_2 = cur_df[['description', 'Verdict', 'Prob']]
# # print(df_2.head())
# cur_list = df_2.values.tolist()
# # print(np.shape(cur_list))
# # cur_list.append()
# # cur_list = []
# cur_db.objects.all().delete()
# # print("==========>Size of the L1 list", len(l1_list))
# for ind, tweet_data in enumerate(cur_list):
#     t = cur_db(tweet = tweet_data[0], res_cls = tweet_data[1], prob_cls = tweet_data[2], res_ent = tweet_data[1], prob_ent = tweet_data[2], iids = "Dummy Image ID",
#                   u1 = "URL dummy", u1res = tweet_data[1], u1prob = tweet_data[2], u2 = "URL dummy", u2res = tweet_data[1], u2prob = tweet_data[2],
#                   u3 = "URL dummy", u3res = tweet_data[1], u3prob = tweet_data[2], u4 = "URL dummy", u4res = tweet_data[1], u4prob = tweet_data[2],
#                   u5 = "URL dummy", u5res = tweet_data[1], u5prob = tweet_data[2], u6 = "URL dummy", u6res = tweet_data[1], u6prob = tweet_data[2],
#                   u7 = "URL dummy", u7res = tweet_data[1], u7prob = tweet_data[2], u8 = "URL dummy", u8res = tweet_data[1], u8prob = tweet_data[2],
#                   u9 = "URL dummy", u9res = tweet_data[1], u9prob = tweet_data[2], u10 = "URL dummy", u10res = tweet_data[1], u10prob = tweet_data[2])
#     t.save()
# print(f"===========>DB {f_name} populated!")
# # # -----------------------------------------------



# Create your views here.
# State-wise codes
s_Code = {'in-py': "Puducherry",
         'in-ld': "Lakshadweep",
         'in-wb': "West_Bengal",
         'in-or': "Orissa",
         'in-br': "Bihar",
         'in-sk': "Sikkim",
         'in-ct': "Chattisgarh",
         'in-tn': "TN",
         'in-mp': "MP",
         'in-2984': "Gujrat",
         'in-ga': "Goa",
         'in-nl': "Nagaland",
         'in-mn': "Manipur",
         'in-ar': "Arunachal_Pradesh",
         'in-mz': "Mizoram",
         'in-tr': "Tripura",
         'in-3464': "Daman_and_Diu",
         'in-dl': "Delhi",
         'in-hr': "Haryana",
         'in-ch': "Chandigarh",
         'in-hp': "HP",
         'in-jk': "J&K",
         'in-kl': "Kerela",
         'in-ka': "Karnataka",
         'in-dn': "Dadra_and_Nagar_Haveli",
         'in-mh': "Maharashtra",
         'in-as': "Assam",
         'in-ap': "AP",
         'in-ml': "Meghalaya",
         'in-pb': "Punjab",
         'in-rj': "Rajasthan",
         'in-up': "UP",
         'in-ut': "Uttaranchal",
         'in-jh': "Jharkhand"}



def index(request):
    return render(request, 'frontend/prediction_V2_V0_blank.html')

def dashboard_index(request):
    # Get the visualization "fake" counts data for Indian cities
    sHist_df = pd.read_csv('/home/shivam/PycharmProjects/Django/Django_Warehouse/todo-django-rest-framework-master/todo_drf/statewise_tweets/stat_numbers_scraped.csv', index_col=[0])
    # Get the last day "fake" counts for Indian cities
    state_lstday_array, last_date = getIndiaGeoData(sHist_df)
    # Get the total "fake" counts for Indian cities and overall
    s_name_sort_list, totals_sort_list, overallFakeCount = getIndiaBarData(sHist_df)
    context = {'state_lstday_array': state_lstday_array, 's_name_sort_list': s_name_sort_list,
               'totals_sort_list': totals_sort_list, 'overallFakeCount': overallFakeCount,
               'last_date': last_date}
    return render(request,'frontend/dashboard_index.html',context)


def trace_landing(request):
    state_form = stateForm()
    state_selected = False
    context = {'state_form': state_form, 'stateFlag': state_selected}
    return render(request, 'frontend/trace_1.html', context)

def trace_1(request):
    state_form = stateForm(request.POST)
    loc = request.POST.get('stateName')
    if loc:
        state_selected = True
    stateName = s_Code[loc]
    top_10_feku_pred, top_10_feku_RT = getIndiaTopFakers(stateName)
    int_lst = np.arange(1, 8)
    # Get the user details for top fake tweeters based on 'prediction'
    feku_list_pred = []
    for feku in top_10_feku_pred:
        feku_dict = {}
        feku_dict["Time_created"] = feku[0]
        feku_dict["username"] = feku[1]
        feku_dict["description"] = feku[2]
        feku_dict["label"] = feku[3]
        feku_dict["prob"] = feku[4]
        feku_dict["src"] = "https://bootdey.com/img/Content/avatar/avatar" + str(
            random.choices(int_lst, k=1)[0]) + ".png"
        feku_list_pred.append(feku_dict)

    # Get the user details for top fake tweeters based on 'retweet count'
    feku_list_RT = []
    fake_med_sec_list = []
    uname_med_sec_dict = dict()
    for ind, feku in enumerate(top_10_feku_RT):
        # print(f"Printing for user {ind}")
        feku_dict = {}
        feku_dict["Tweet_ID"] = feku[0]
        feku_dict["Time_created"] = feku[1]
        feku_dict["username"] = feku[2]
        feku_dict["description"] = feku[3]
        feku_dict["label"] = feku[4]
        feku_dict["retweetcount"] = feku[5]
        feku_dict["src"] = "https://bootdey.com/img/Content/avatar/avatar" + str(
            random.choices(int_lst, k=1)[0]) + ".png"
        # print("Top RT feku Dictionary populated for this user, checking for retweeter IDs...")
        in_id = feku_dict["Tweet_ID"]
        # print(f"Checking for the tweet: {in_id} with type {type(in_id)}")
        CONSUMER_KEY = "Vw1I28kAqmtlR6bxxWC4XRotQ"
        CONSUMER_SECRET = "5BWJpsp7I7flL7A2s6UHKbfkc1CNcJun0oTcBQLpbbAYf5bLux"
        OAUTH_TOKEN = "2457738439-exMpEGlgXiCGMIkdPZ55UzjYZnTDUMWQjJGo6at"
        OAUTH_TOKEN_SECRET = "AYG1URNodgVYONyCXyIgsPBiuwWRLCzy7D29WO0kRNFQE"
        # CONSUMER_KEY = "cM593dZzYf2E5iWAWAY5DLYh1"
        # CONSUMER_SECRET = "mtbmruUaGbyct7E1gE9jFBiosL0IoLHsvDCVhnfFru3I8oBRFA"
        # OAUTH_TOKEN = "4827039441-TGPGL0EOa0Eflp2LoEGgelaIhd5IijBzYi4A5aL"
        # OAUTH_TOKEN_SECRET = "T9M1ynlEW89mqlolZjbcHo08InzLbKgcqPNxMd0UFg7Aj"
        # CONSUMER_KEY = "gp8cEMcGZafEqB9RfOiHrLEod"
        # CONSUMER_SECRET = "uo78v5nFF3cjc2gSjkpPDL3XpIqUvXZ5qJ7FIMx3VNVOkIJPRX"
        # OAUTH_TOKEN = "4827125495-Ujpubs7jfxyDanohxq2PtpeRXFnqladYBNuMdEd"
        # OAUTH_TOKEN_SECRET = "0FMAcYWtLJvQYzf7LJjKQwbzrKEJDtLEa99iyRNGUNBWK"
        twitter = Twython(
            CONSUMER_KEY, CONSUMER_SECRET,
            OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

        retweets = twitter.get_retweets(id=in_id, count=100)
        username_time_list = []
        if len(retweets):
            if len(retweets)==1:
                # Dummy value for now, need to update using the difference from the priginal tweet
                cur_fake_med_sec = (dateutil.parser.parse(retweets[0]['created_at'])-dateutil.parser.parse(feku_dict["Time_created"])).total_seconds()
                uname_med_sec_dict[feku_dict["username"]] = cur_fake_med_sec
            else:
                tot_secdiff_list=[]
                for i, rt in enumerate(retweets):
                    rt_toc = rt['created_at']
                    # rt_id = rt['Tweet_ID']
                    # rt_user_id = rt['user']['Tweet_ID']
                    rt_user_name = rt['user']['name']
                    rt_user_scrname = rt['user']['screen_name']
                    # rt_user_loc = rt['user']['location']
                    username_time_list.append({'rt_user_scrname': rt_user_scrname, 'rt_user_name': rt_user_name, 'rt_toc': rt_toc})
                    if i < len(retweets) - 1:
                        cur_tot_sec = (dateutil.parser.parse(retweets[i]['created_at']) - dateutil.parser.parse(
                            retweets[i + 1]['created_at'])).total_seconds()
                        # print(cur_tot_sec)
                        tot_secdiff_list.append(cur_tot_sec)
                cur_fake_med_sec = np.median(tot_secdiff_list)
                uname_med_sec_dict[feku_dict["username"]] = cur_fake_med_sec
            feku_dict["feku_retweeters"] = username_time_list
            fake_med_sec_list.append(cur_fake_med_sec)
        else:
            feku_dict["feku_retweeters"] = ['No Retweet details found']
        # rt_ids = twitter.get_retweeters_ids(id=in_id, count=100)
        # print(f"A total of {len(rt_ids['ids'])} ids found.\n{rt_ids}\nChecking for screen names...")
        # if len(rt_ids['ids']):
        #     sampleids = [str(i) for i in rt_ids['ids']]
        #     comma_separated_string = ",".join(sampleids)
        #     output = twitter.lookup_user(user_id=comma_separated_string)
        #     # print(f"Retweeter details list shown below: \n{output}")
        #     username_time_list = []
        #     for user in output:
        #         username_time_list.append({'screen_name': user['screen_name'], 'rt_time': user['created_at']})
        #     feku_dict["feku_retweeters"] = username_time_list
        #     print(f"Retweeter names list shown below: \n{username_time_list}")
        # else:
        #     feku_dict["feku_retweeters"] = ['No Retweet details found']
        # feku_dict["RT"] = len(retweets)
        feku_list_RT.append(feku_dict)
    # for feku in top_10_feku_RT:
    #     feku_dict = {}
    #     feku_dict["Time_created"] = feku[0]
    #     feku_dict["username"] = feku[1]
    #     feku_dict["description"] = feku[2]
    #     feku_dict["label"] = feku[3]
    #     feku_dict["retweetcount"] = feku[4]
    #     feku_dict["src"] = "https://bootdey.com/img/Content/avatar/avatar" + str(
    #         random.choices(int_lst, k=1)[0]) + ".png"
    #     feku_list_RT.append(feku_dict)
    # print(f"=====>Median for seconds diff for this session: \n{fake_med_sec_list}")
    uname_med_sec_dict_sort = {k: v for k, v in sorted(uname_med_sec_dict.items(), key=lambda item: item[1])}
    # print("=======>uname_med_sec_dict_sort")
    uname_sort_list=[]
    med_sec_sort_list=[]
    for k,v in uname_med_sec_dict_sort.items():
        uname_sort_list.append(k)
        med_sec_sort_list.append(v)
        print(k,v)
    m_max = max(med_sec_sort_list)
    med_sec_sort_list_norm = [float(i) / m_max for i in med_sec_sort_list]
    # med_sec_sort_list_norm_inv = np.round(list(np.log(1/np.array(med_sec_sort_list_norm))+sys.float_info.epsilon), 2)
    med_sec_sort_list_norm_inv = list(np.log(1 / np.array(med_sec_sort_list_norm)) + sys.float_info.epsilon)
    # print(f"norm: {med_sec_sort_list_norm}")
    # print(f"norm inv: {med_sec_sort_list_norm_inv}")
    #
    # # Dummy variables
    # uname_sort_list = ['name1', 'name2', 'name3', 'name4']
    # med_sec_sort_list_norm_inv = [0.6, 0.3, 0.2, 0.1]
    uname_med_sec_list_dict = {'username': uname_sort_list, 'med_sec_sort_list': med_sec_sort_list_norm_inv}
    context = {'state_form': state_form, 'feku_list_pred': feku_list_pred, 'feku_list_RT': feku_list_RT, 'uname_med_sec_list_dict': uname_med_sec_list_dict, 'stateFlag': state_selected, 'location': stateName}
    return render(request, 'frontend/trace_1.html', context)

def get_city_df(in_state = None):
    lab_lst = ['real', 'fake']
    base_df = pd.read_csv('~/PycharmProjects/Django/Django_Warehouse/todo-django-rest-framework-master/todo_drf/statewise_tweets/'+in_state+'_Tweets.csv')
    N = len(base_df)
    base_df_city = base_df[['Tweet_ID', 'Time_created', 'username', 'description', 'retweetcount']]
    df1 = base_df_city
    # Assign the random labels
    df1['label'] = random.choices(lab_lst, weights=(0.7, 0.3), k=N)

    # # Get the real/fake predictions
    # label_list = []
    # for item in df1['description']:
    #     cur_res = proc_classification(item)
    #     print(f"Result for\n{item}\n{cur_res}")
    #     label_list.append(cur_res)
    # df1['label'] = label_list


    hour_list = df1['Time_created'].transform(lambda x: dateutil.parser.parse(x).hour).tolist()
    day_list = df1['Time_created'].transform(lambda x: dateutil.parser.parse(x).day).tolist()
    month_list = df1['Time_created'].transform(lambda x: dateutil.parser.parse(x).month).tolist()
    year_list = df1['Time_created'].transform(lambda x: dateutil.parser.parse(x).year).tolist()
    df1['hour'] = hour_list
    df1['day'] = day_list
    df1['month'] = month_list
    df1['year'] = year_list
    randomproblist = []
    for i in range(0, len(base_df_city)):
        n = np.round(random.uniform(0, 1), 2)
        randomproblist.append(n)
    df1['prob'] = randomproblist

    # # Creating a list of retweet values for the given dataframe
    # # half will be 0; remaining will be numbers
    # # print(f"Total {N}")
    # zeros = np.zeros(N // 2).tolist()
    # # print(f"Zeros: {len(zeros)}")
    # int_lst = np.arange(1, 21)
    # # print(int_lst)
    # rt_list = random.choices(int_lst, k=(N - N // 2))
    # # print(f"RT List: {len(rt_list)}")
    # new_rt_list = zeros + rt_list
    # random.shuffle(new_rt_list)
    # random.shuffle(new_rt_list)
    # # # Random RT generation list
    # # new_rt_list = [int(x) for x in new_rt_list]
    # # # print(new_rt_list[:20])
    # # df1['RT'] = new_rt_list
    return df1


def getIndiaTopFakers(in_state):
    df1 = get_city_df(in_state)
    top_10_feku_pred = df1[df1['label']=='fake'][['Time_created', 'username', 'description', 'label', 'prob']].sort_values(by='prob', ascending=False)[:10].values.tolist()
    top_10_feku_RT = df1[df1['label'] == 'fake'][['Tweet_ID', 'Time_created', 'username', 'description', 'label', 'retweetcount']].sort_values(by='retweetcount', ascending=False)[:10].values.tolist()
    return top_10_feku_pred, top_10_feku_RT

def getIndiaGeoData(sHist_df):
    state_lstday_array = sHist_df[['country_code', sHist_df.columns[-1]]].values.tolist()
    last_date = sHist_df.columns[-1]
    return (state_lstday_array, last_date)
def getIndiaBarData(sHist_df):
    tot_list = sHist_df[sHist_df.columns[1:]].sum(axis=1, skipna=True).tolist()
    s_tot_df = sHist_df['country_code'].to_frame(name='country_code')
    s_tot_df['totals'] = tot_list
    s_tot_sort_df = s_tot_df.sort_values(by='totals', ascending=False).reset_index().drop('index', axis=1)
    s_tot_sort_df.head()
    state_sort_list = s_tot_sort_df['country_code'].tolist()
    s_name_sort_list = []
    for state in state_sort_list:
        s_name_sort_list.append(s_Code[state])
    totals_sort_list = s_tot_sort_df['totals'].tolist()
    overallFakeCount = np.sum(totals_sort_list)
    return (s_name_sort_list, totals_sort_list, overallFakeCount)

def showRT(request):
    print(request.POST.dict())
    # Line chart data for Indian scenario
    source_id = request.POST.get('trace')
    if source_id:
        # populate the RT list
        RT_list = ['RTweeter1', 'RTweeter2', 'RTweeter3', 'RTweeter4', 'RTweeter5']
    context = {'rt_people_list': RT_list, 'source': source_id}
    return render(request,'frontend/trace_2.html',context)

def drillDownAState(request):
    print (request.POST.dict())
    # Line chart data for Indian scenario
    stateName=request.POST.get('stateName')
    df1 = get_city_df(stateName)
    # =========================================================================
    # Hourly Aspects
    # =========================================================================
    df2_h = df1.groupby(by=['year', 'month', 'day', 'hour', 'label']).size().to_frame(name='count').sort_values(
        by=['year', 'month', 'day', 'hour']).reset_index()
    grouped_h = df2_h.groupby(by=['year', 'month', 'day', 'hour'])
    # print(len(grouped))
    fake_count_list_h = []
    real_count_list_h = []
    for name, group in grouped_h:
        #     print(name)
        #     print(group)
        if len(group[group['label'] == 'fake']['count']):
            cnt_fk = group[group['label'] == 'fake']['count'].tolist()[0]
            fake_count_list_h.append(cnt_fk)
        else:
            fake_count_list_h.append(0)
        #     print(f"Fake list: {fake_count_list}")
        if len(group[group['label'] == 'real']['count']):
            cnt_rl = group[group['label'] == 'real']['count'].tolist()[0]
            real_count_list_h.append(cnt_rl)
        else:
            real_count_list_h.append(0)
    #     print(f"Real list: {real_count_list}")

    # print(len(fake_count_list_h))
    # print(len(real_count_list_h))

    df3_h = df2_h[['year', 'month', 'day', 'hour']].drop_duplicates()
    # print(len(df3_h))
    df3_h['real'] = real_count_list_h
    df3_h['fake'] = fake_count_list_h
    df4_h = df1.groupby(by=['year', 'month', 'day', 'hour']).size().to_frame(name='count').sort_values(
        by=['year', 'month', 'day', 'hour']).reset_index()
    total_list_h = df4_h['count'].tolist()
    df3_h['total'] = total_list_h
    df3_h.head()
    ts_list_h = (df3_h['year'].map(str) + '-' + df3_h['month'].map(str) + '-' + df3_h['day'].map(str) + '-' + df3_h[
        'hour'].map(str)).tolist()
    # print (ts_list_h)
    df3_h['timestamp'] = ts_list_h
    df5_h = df3_h.drop(["year", "month", "day", "hour"], axis=1)
    hourly_df = df5_h[['timestamp', 'real', 'fake', 'total']]
    # hourly_df.head()
    data_tweet_h = [{'label': 'Hourly Total Tweets', 'data': hourly_df['total'].values.tolist(), 'borderColor': '#03a9fc',
                   'backgroundColor': '#03a9fc', 'fill': 'false'},
                  {'label': 'Hourly Fake Tweets', 'data': hourly_df['fake'].values.tolist(), 'borderColor': '#ff6384',
                   'backgroundColor': '#ff6384', 'fill': 'false'}]


    # =========================================================================
    # Daily Aspects for visualization
    # =========================================================================
    df2 = df1.groupby(by=['year', 'month', 'day', 'label']).size().to_frame(name='count').sort_values(
        by=['year', 'month', 'day']).reset_index()
    grouped = df2.groupby(by=['year', 'month', 'day'])
    # print(len(grouped))
    fake_count_list = []
    real_count_list = []
    for name, group in grouped:
        #     print(name)
        #     print(group)
        if len(group[group['label'] == 'fake']['count']):
            cnt_fk = group[group['label'] == 'fake']['count'].tolist()[0]
            fake_count_list.append(cnt_fk)
        else:
            fake_count_list.append(0)
        #     print(f"Fake list: {fake_count_list}")
        if len(group[group['label'] == 'real']['count']):
            cnt_rl = group[group['label'] == 'real']['count'].tolist()[0]
            real_count_list.append(cnt_rl)
        else:
            real_count_list.append(0)
    #     print(f"Real list: {real_count_list}")

    # print(len(fake_count_list))
    # print(len(real_count_list))
    df3 = df2[['year', 'month', 'day']].drop_duplicates()
    # print(len(df3))
    df3['real'] = real_count_list
    df3['fake'] = fake_count_list
    df4 = df1.groupby(by=['year', 'month', 'day']).size().to_frame(name='count').sort_values(
        by=['year', 'month', 'day']).reset_index()
    total_list = df4['count'].tolist()
    df3['total'] = total_list
    df3.head()
    ts_list = (df3['year'].map(str) + '-' + df3['month'].map(str) + '-' + df3['day'].map(str)).tolist()
    # print (ts_list)
    df3['timestamp'] = ts_list
    df5 = df3.drop(["year", "month", "day"], axis=1)
    daily_df = df5[['timestamp', 'real', 'fake', 'total']]
    # daily_df.head()
    data_tweet = [{'label':'Daily Total Tweets','data':daily_df['total'].values.tolist(),'borderColor':'#03a9fc','backgroundColor':'#03a9fc','fill':'false'},
                  {'label':'Daily Fake Tweets','data':daily_df['fake'].values.tolist(),'borderColor':'#ff6384','backgroundColor':'#ff6384','fill':'false'}]


    # =========================================================================
    # Monthly Aspects for visualization
    # =========================================================================
    df2_m = df1.groupby(by=['year', 'month', 'label']).size().to_frame(name='count').sort_values(
        by=['year', 'month']).reset_index()
    grouped_m = df2_m.groupby(by=['year', 'month'])
    print(len(grouped_m))
    fake_count_list_m = []
    real_count_list_m = []
    for name, group in grouped_m:
        #     print(name)
        #     print(group)
        if len(group[group['label'] == 'fake']['count']):
            cnt_fk = group[group['label'] == 'fake']['count'].tolist()[0]
            fake_count_list_m.append(cnt_fk)
        else:
            fake_count_list_m.append(0)
        #     print(f"Fake list: {fake_count_list}")
        if len(group[group['label'] == 'real']['count']):
            cnt_rl = group[group['label'] == 'real']['count'].tolist()[0]
            real_count_list_m.append(cnt_rl)
        else:
            real_count_list_m.append(0)
    #     print(f"Real list: {real_count_list}")

    # print(len(fake_count_list_m))
    # print(len(real_count_list_m))
    df3_m = df2_m[['year', 'month']].drop_duplicates()
    # print(len(df3))
    df3_m['real'] = real_count_list_m
    df3_m['fake'] = fake_count_list_m
    df4_m = df1.groupby(by=['year', 'month']).size().to_frame(name='count').sort_values(
        by=['year', 'month']).reset_index()
    total_list_m = df4_m['count'].tolist()
    df3_m['total'] = total_list_m
    # print(df3_m.head())

    # Monthly data
    ts_list_m = (df3_m['year'].map(str) + '-' + df3_m['month'].map(str)).tolist()
    # print (ts_list_m)
    df3_m['timestamp'] = ts_list_m
    df5_m = df3_m.drop(["year", "month"], axis=1)
    monthly_df = df5_m[['timestamp', 'real', 'fake', 'total']]
    # print(monthly_df.head())

    data_tweet_m = [{'label': 'Monthly Total Tweets', 'data': monthly_df['total'].values.tolist(), 'borderColor': '#03a9fc',
                   'backgroundColor': '#03a9fc', 'fill': 'false'},
                  {'label': 'Monthly Fake Tweets', 'data': monthly_df['fake'].values.tolist(), 'borderColor': '#ff6384',
                   'backgroundColor': '#ff6384', 'fill': 'false'}]
    sHist_df = pd.read_csv('/home/shivam/PycharmProjects/Django/Django_Warehouse/todo-django-rest-framework-master/todo_drf/statewise_tweets/stat_numbers_scraped.csv', index_col=[0])
    s_name_sort_list, totals_sort_list, overallFakeCount = getIndiaBarData(sHist_df)
    context={'axisvalues':daily_df['timestamp'].values.tolist(),
             'axisvalues_m':monthly_df['timestamp'].values.tolist(), 'axisvalues_h':hourly_df['timestamp'].values.tolist(),
             'data_tweet': data_tweet, 'data_tweet_m': data_tweet_m, 'data_tweet_h': data_tweet_h, "stateName":stateName,
             's_name_sort_list': s_name_sort_list, 'totals_sort_list': totals_sort_list, 'overallFakeCount': overallFakeCount}
    return render(request,'frontend/dashboard_drill.html',context)
def stat(request):
    return render(request, 'frontend/statistics.html')

def about(request):
    return render(request, 'frontend/aboutus.html')

def frame_1_blank(request, cnt):
    # Push raw tweets into the DB
    # print("===========>Pushing RAW data into DB")
    # # PC = PredictorConfig(loc)
    # TRAW = PredictorConfig.tweets_raw
    # iid_list = PredictorConfig.iids
    # Tweets.objects.all().delete()
    # for ind, tweet in enumerate(TRAW):
    #     t = Tweets(tweet_text=tweet, iids=iid_list[ind])
    #     t.save()
    # print("===========>DB populated!")
    context = {'proc_status': False, 'first_disp': True}
    return render(request, 'frontend/frame_1_blank.html', context)



def frame_1(request, uri):
    uri_content = uri.split('&')
    cur_dict = dict()
    for item in uri_content:
        key_val = item.split('=')
        cur_dict[key_val[0]] = key_val[1]
    loc = cur_dict['loc']
    context = {'loc': loc, 'proc_status': True, 'first_disp': False}
    return render(request, 'frontend/frame_1.html', context)

def frame_2_blank(request, cnt):
    # print("==============Inside frame_2_blank=================")
    # # Push filtered tweets into the DB
    # print("===========>Pushing L1 data into DB")
    # l1_list = PredictorConfig.data_l1_list_demo
    # Tweets_L1.objects.all().delete()
    # print("==========>Size of the L1 list", len(l1_list))
    # for tweet_data in l1_list:
    #     t = Tweets_L1(tweets = tweet_data[0],direct_claim = tweet_data[1],direct_claim_probability = tweet_data[2],indirect_claim = tweet_data[3],indirect_claim_probability = tweet_data[4],opinion = tweet_data[5],opinion_probability = tweet_data[6],quote = tweet_data[7],quote_probability = tweet_data[8],not_claim = tweet_data[9],not_claim_probability = tweet_data[10], iids = tweet_data[14])
    #     t.save()
    # # print("===========>DB populated!")
    context = {'proc_status': False, 'first_disp': True}
    return render(request, 'frontend/frame_2_blank.html', context)



def frame_2(request, uri):
    print("==========>Pritning LOCATION content in frame2 view")
    print(uri)
    uri_content = uri.split('&')
    cur_dict = dict()
    for item in uri_content:
        key_val = item.split('=')
        cur_dict[key_val[0]] = key_val[1]
    loc = cur_dict['loc']
    context = {'loc': loc, 'proc_status': True, 'first_disp': False}
    # print("The data is:")
    # print(l2_Data)
    return render(request, 'frontend/frame_2.html', context)

def frame_3_blank(request, cnt):
    print("==============Inside frame_3_blank=================")
    # Push filtered tweets into the DB
    # print("===========>Pushing L2 data into DB")
    # l2_list = PredictorConfig.data_l2_list_demo
    # Tweets_L2.objects.all().delete()
    # print("==========>Size of the L1 list", len(l2_list))
    # for tweet_data in l2_list:
    #     t = Tweets_L2(tweets = tweet_data[0],direct_claim = tweet_data[1],direct_claim_probability = tweet_data[2],indirect_claim = tweet_data[3],indirect_claim_probability = tweet_data[4],opinion = tweet_data[5],opinion_probability = tweet_data[6],quote = tweet_data[7],quote_probability = tweet_data[8],not_claim = tweet_data[9],not_claim_probability = tweet_data[10], level_2 = tweet_data[11], level_2_probability = tweet_data[12], iids = tweet_data[14])
    #     t.save()
    # print("===========>DB populated!")
    context = {'proc_status': False, 'first_disp': True}
    return render(request, 'frontend/frame_3_blank.html', context)


def frame_3(request, uri):
    uri_content = uri.split('&')
    cur_dict = dict()
    for item in uri_content:
        key_val = item.split('=')
        cur_dict[key_val[0]] = key_val[1]
    loc = cur_dict['loc']
    context = {'loc': loc, 'proc_status': True, 'first_disp': False}
    # print("The data is:")
    # print(l2_Data)
    return render(request, 'frontend/frame_3.html', context)


#================= FRAME 4=============================

def frame_4_blank(request):
    f_obj1 = locationForm()

    # print("==============Inside frame_4_blank=================")
    # # Push filtered tweets into the DB
    # print("===========>Pushing L3 data into DB")
    # ent_list = PredictorConfig.ent_list
    # entaildata.objects.all().delete()
    # print("==========>Size of the Entail list", len(ent_list))
    # for tweet_data in ent_list:
    #     t_len = len(tweet_data)
    #     if t_len<14:
    #         new_temp_list=[]
    #         for x in range(14-t_len):
    #             new_temp_list.append("--")
    #         tweet_data=tweet_data+new_temp_list
    #     print(len(tweet_data))
    #     print(tweet_data)
    #     t = entaildata(tweet = tweet_data[0],FNF = tweet_data[1], prob = tweet_data[2], iids = tweet_data[3], u1 = tweet_data[4], u2 = tweet_data[5], u3 = tweet_data[6], u4 = tweet_data[7], u5 = tweet_data[8], u6 = tweet_data[9], u7 = tweet_data[10], u8 = tweet_data[11], u9 = tweet_data[12], u10 = tweet_data[13])
    #     t.save()
    # print("===========>DB populated!")
    context = {'proc_status': False, 'first_disp': True, 'form': f_obj1}
    return render(request, 'frontend/frame_4_blank.html', context)
# Location INDEPENDENT (for demo pusposes) frame 4 display
def frame_4(request):
    loc_set = False
    loc = None
    if request.method == 'POST':
        if request.POST.get("stop_btn"):
            f_obj = locationForm()
            response = {'f': 0, 'form': f_obj, 'loc': loc,
                        'first_disp': False, 'proc_status': loc_set}
            return render(request, 'frontend/frame_4_blank.html', response)
        temp = 'frontend/frame_4.html'
        loc_set = True
        f_obj = locationForm(request.POST)
        loc = request.POST.get('location')
        response = {'f': 1, 'form': f_obj, 'loc': loc, 'first_disp': False, 'proc_status': loc_set}
    else:
        temp = 'frontend/frame_4_blank.html'
        f_obj = locationForm()
        response = {'f': 0, 'form': f_obj, 'loc': loc, 'first_disp': True, 'proc_status': loc_set}
    return render(request, temp, response)

    # # Earlier simpler implementation without stop
    # # -------------------------------------------------------------
    # print("Inside frame 4 for further evaluation:")
    # print(request.POST)
    # loc = request.POST.get('location')
    # # loc = 'DLI'
    # context = {'loc': loc, 'proc_status': True, 'first_disp': False}
    # # print("The data is:")
    # # print(l2_Data)
    # return render(request, 'frontend/frame_4.html', context)

# Location specific frame 4 display
# def frame_4(request, uri):
#     uri_content = uri.split('&')
#     cur_dict = dict()
#     for item in uri_content:
#         key_val = item.split('=')
#         cur_dict[key_val[0]] = key_val[1]
#     loc = cur_dict['loc']
#     context = {'loc': loc, 'proc_status': True, 'first_disp': False}
#     # print("The data is:")
#     # print(l2_Data)
#     return render(request, 'frontend/frame_4.html', context)


def frame_5_blank(request, cnt):
    # print("==============Inside frame_4_blank=================")
    # # Push filtered tweets into the DB
    # print("===========>Pushing L3 data into DB")
    # l3_list_demo = PredictorConfig.data_l3_list_demo
    # Tweets_L3.objects.all().delete()
    # print("==========>Size of the L3 list", len(l3_list_demo))
    # for tweet_data_demo in l3_list_demo:
    #     if tweet_data_demo[11]=='fact_check':
    #         l2p_demo = tweet_data_demo[12]
    #     else:
    #         l2p_demo = tweet_data_demo[12][0]
    #     t_demo = Tweets_L3(tweets = tweet_data_demo[0],direct_claim = tweet_data_demo[1],direct_claim_probability = tweet_data_demo[2],indirect_claim = tweet_data_demo[3],indirect_claim_probability = tweet_data_demo[4],opinion = tweet_data_demo[5],opinion_probability = tweet_data_demo[6],quote = tweet_data_demo[7],quote_probability = tweet_data_demo[8],not_claim = tweet_data_demo[9],not_claim_probability = tweet_data_demo[10], level_2 = tweet_data_demo[11], level_2_probability = l2p_demo, level_3_tag = tweet_data_demo[13], iids = tweet_data_demo[14])
    #     t_demo.save()

    # l3_list_city = PredictorConfig.data_l3_list_city
    # fact_dli.objects.all().delete()
    # print("==========>Size of the L3 list", len(l3_list_city))
    # for tweet_data_city in l3_list_city:
    #     # print("Facetcheck/Pass: ",tweet_data_city[11])
    #     # print("L2 prob", tweet_data_city[12])
    #     # print(tweet_data_city)
    #     if tweet_data_city[11] == 'fact_check':
    #         l2p_city = tweet_data_city[12]
    #     else:
    #         try:
    #             l2p_city = tweet_data_city[12][0]
    #         except:
    #             l2p_city = 0
    #     t_city = fact_dli(tweets=tweet_data_city[0], direct_claim=tweet_data_city[1],
    #                   direct_claim_probability=tweet_data_city[2], indirect_claim=tweet_data_city[3],
    #                   indirect_claim_probability=tweet_data_city[4], opinion=tweet_data_city[5],
    #                   opinion_probability=tweet_data_city[6], quote=tweet_data_city[7],
    #                   quote_probability=tweet_data_city[8], not_claim=tweet_data_city[9],
    #                   not_claim_probability=tweet_data_city[10], level_2=tweet_data_city[11], level_2_probability=l2p_city,
    #                   level_3_tag=tweet_data_city[13], iids=tweet_data_city[14])
    #     t_city.save()
    # print("===========>DB populated!")
    context = {'proc_status': False, 'first_disp': True}
    return render(request, 'frontend/frame_5_blank.html', context)


def frame_5(request, uri):
    uri_content = uri.split('&')
    cur_dict = dict()
    for item in uri_content:
        key_val = item.split('=')
        cur_dict[key_val[0]] = key_val[1]
    loc = cur_dict['loc']
    context = {'loc': loc, 'proc_status': True, 'first_disp': False}
    # print("The data is:")
    # print(l2_Data)
    return render(request, 'frontend/frame_5.html', context)




def start_disp(request):
    # print("In the start disp")
    # train_set = ['item 101', 'item 102', 'item 103', 'item 104', 'item 105', 'item 106', 'item 107', 'item 108', 'item 109', 'item 110']
    # test_set = ['item 1', 'item 2', 'item 3', 'item 4', 'item 5']
    # sel_set = ['item 4', 'item 5']
    # response = {'l1': train_set, 'l2': test_set, 'l3': sel_set}
    loc_set=False
    loc=None
    if request.method=='POST':
        temp = 'frontend/prediction_V2_V0.html'
        if request.POST.get("stop_btn"):
            # print("===============>In the stop rule")
            f_obj1 = locationForm()
            # f_obj2 = UploadFileForm()
            # response = {'f1': 0, 'f2': 0, 'f3': 0, 'f4': 0, 'f5': 0, 'form1': f_obj1, 'form2': f_obj2, 'loc': loc, 'first_disp': False, 'loc_flag': loc_set}
            response = {'f1': 0, 'f2': 0, 'f3': 0, 'f4': 0, 'f5': 0, 'form1': f_obj1, 'loc': loc,
                        'first_disp': False, 'loc_flag': loc_set}
            return render(request, 'frontend/prediction_V2_V0_First.html', response)
        loc_set=True
        f_obj1 = locationForm(request.POST)
        # f_obj2 = UploadFileForm(request.POST, request.FILES)
        # print("=============>File Name", request.POST.get('file', False))
        # f_len = len(request.POST.get('file', False))
        loc = request.POST.get('location')
        # if f_obj2.is_valid():
        #     print("File form is totally valid!")
        #     if f_len!=0 and loc=='OTR':
        #         loc = 'DEMO'
        #         print('location set to DEMO')
        #     else:
        #         print('Location stays the same')
        #     handle_uploaded_file(request.FILES['file'])

        # print("==============>Location", loc)
        # Initializing the category-wise count
        # f_stat = PredictorConfig.final_stat
        f_stat = [10, 0, 0, 0, 0, 90, 0, 0, 0, 90]
        f_stat1 = f_stat[0:3]
        f_stat2 = f_stat[3:6]
        f_stat3 = f_stat[6:9]
        cat_tag1 = ['Rumors', 'Authorities', 'Fake Cure']
        cat_tag2 = ['Religious', 'Panic', 'Others']
        cat_tag3 = ['Political', 'Racist', 'Xenophobic']
        lst1 = zip(cat_tag1, f_stat1)
        lst2 = zip(cat_tag2, f_stat2)
        lst3 = zip(cat_tag3, f_stat3)
        # print("=====start_disp========>FSTAT", f_stat)
        my_dict = {'loc': loc, 'first_disp': True}
        uri = urllib.parse.urlencode(my_dict)
        # 'fstat1': f_stat1, 'fstat2': f_stat2,
        # 'fstat3': f_stat3, 'cat_list1': cat_tag1, 'cat_list2': cat_tag2, 'cat_list3': cat_tag3
        # response = {'f1': 1, 'f2': 1, 'f3': 1, 'f4': 1, 'f5': 1,
        #             'form1': f_obj1, 'form2': f_obj2, 'uri': uri, 'loc_flag': loc_set,
        #             'fstat1': lst1, 'fstat2': lst2, 'fstat3': lst3}
        response = {'f1': 1, 'f2': 1, 'f3': 1, 'f4': 1, 'f5': 1,
                    'form1': f_obj1, 'uri': uri, 'loc_flag': loc_set,
                    'fstat1': lst1, 'fstat2': lst2, 'fstat3': lst3}
        # print("=========>Handling the POST here (loc)")
        # print()
        # print(loc)
        # my_dict = {'f1': 1, 'loc': loc}
        # uri = urllib.parse.urlencode(my_dict)
        # fullurl = your_server_url + "/?" + uri
        # response = {'dict_str': uri, 'f2': 0, 'f3': 0, 'form': f_obj1}
    else:
        temp = 'frontend/prediction_V2_V0_First.html'
        f_obj1 = locationForm()
        f_obj2 = UploadFileForm()
        # my_dict = {'f1': 0, 'loc': None}
        # uri = urllib.parse.urlencode(my_dict)
        # response = {'dict_str': uri, 'f2': 0, 'f3': 0, 'form': f_obj1}
        response = {'f1': 0, 'f2': 0, 'f3': 0, 'f4': 0, 'f5': 0, 'form1': f_obj1, 'form2': f_obj2, 'loc': loc, 'first_disp': True, 'loc_flag': loc_set}
    # YOUR_OBJECT.objects.filterprediction_V2(pk=pk).update(views=F('views')+1)
    # print("===========>Just before dispatching")
    # print(response)
    return render(request, temp, response)

def proc_classification(in_text):
    res, pro = FrontendAppConfig.text_FNF_classify([in_text])
    result = res[0]
    prob = pro[0]
    return result, prob

def proc_entailment(in_text):
    print("===========>Entailment module called")
    result = PredictorConfig.fake_verdict(in_text)
    print(result)
    return result

# On button click backend module to be called, for each tweet in stream and check
@api_view(['GET'])
def contact_F2B_CLS(request, in_text):
    print(request.GET)
    # print(request.POST)
    print("=========*Backend functionality (CLS) accessed! Success*======", str.replace(in_text, '%20', ' '))
    # Logic for Fake news detection/entailment
    # -------Result_class = get_classification_results()
    # -------Result_ent = get_entailment_results()

    Result, prob = proc_classification(in_text)
    # out_list = ["URL1", "URL2", "URL3", "URL4", "URL5", "URL6", "URL7", "URL8", "URL9","URL10"]
    Res_Json = {'Tweet': in_text, 'Result': Result, 'prob': prob}
    return Response(Res_Json)


@api_view(['GET'])
def contact_F2B_ENT(request, in_text):
    print(request.GET)
    # print(request.POST)
    print("=========*Backend functionality (ENT) accessed! Success*======", str.replace(in_text, '%20', ' '))
    # Logic for Fake news detection/entailment
    # -------Result_class = get_classification_results()
    # -------Result_ent = get_entailment_results()
    Result = proc_entailment(in_text)
    print(f"==========>Returned updated final entailment verdict: {Result}")
    # out_list = Result[2:]
    # Res_Json = {'Tweet': in_text, 'Result': Result[0], 'o_lst': out_list}
    # Res_Json = {'Tweet': in_text, 'Result': Result, 'o_lst': out_list}
    return Response(Result)


def render_manual_page(request):
    form = in_textForm(request.POST)
    context = {'proc_done': False, 'form': form}
    return render(request, 'frontend/manual.html', context)

def manual_check_now(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and popclassificationulate it with data from the request:
        form = in_textForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            in_text = form.cleaned_data['in_text']
            choice = form.cleaned_data['check_fields']
            print("=============>The choice is : ", choice)
            ent_flag = False
            fake_flag = False
            if choice=="1":
                ent_flag = True
                Res = proc_entailment(in_text)
                if Res['Result'] == 'Fake':
                    fake_flag = True
            else:
                Res = proc_classification(in_text)
                if Res == 'Fake':
                    fake_flag = True
            out_info = Res
            form = in_textForm()
            context = {'proc_done': True, 'out_info': out_info, 'form': form, 'in_text': in_text, 'ent_flag': ent_flag, 'fake_flag': fake_flag}
            # redirect to a new URL:
            return render(request, 'frontend/manual.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = in_textForm()

    return render(request, 'frontend/manual.html', {'form': form})