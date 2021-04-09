from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import locationForm, UploadFileForm
from .apps import FrontendConfig
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


from api.models import Task, Tweets, Tweets_L1, Tweets_L2, Tweets_L3, entaildata, fact_dli

# Create your views here.

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
    sHist_df = pd.read_csv('statewise_180days_fake_india.csv', index_col=[0])
    # Get the last day "fake" counts for Indian cities
    state_lstday_array, last_date = getIndiaGeoData(sHist_df)
    # Get the total "fake" counts for Indian cities and overall
    s_name_sort_list, totals_sort_list, overallFakeCount = getIndiaBarData(sHist_df)


    # Get the user details for top fake tweeters based on 'prediction'
    top_10_feku_pred, top_10_feku_RT = getIndiaTopFakers()
    feku_list_pred = []
    int_lst=np.arange(1,8)
    for feku in top_10_feku_pred:
        feku_dict={}
        feku_dict["time"] = feku[0]
        feku_dict["uname"] = feku[1]
        feku_dict["tweet"] = feku[2]
        feku_dict["label"] = feku[3]
        feku_dict["prob"] = feku[4]
        feku_dict["src"] = "https://bootdey.com/img/Content/avatar/avatar"+str(random.choices(int_lst, k=1)[0])+".png"
        feku_list_pred.append(feku_dict)

    feku_list_RT = []
    for feku in top_10_feku_RT:
        feku_dict = {}
        feku_dict["time"] = feku[0]
        feku_dict["uname"] = feku[1]
        feku_dict["tweet"] = feku[2]
        feku_dict["label"] = feku[3]
        feku_dict["RT"] = feku[4]
        feku_dict["src"] = "https://bootdey.com/img/Content/avatar/avatar" + str(
            random.choices(int_lst, k=1)[0]) + ".png"
        feku_list_RT.append(feku_dict)




    # print("Total sum is : {}".format(overallFakeCount))

    context = {'state_lstday_array': state_lstday_array, 's_name_sort_list': s_name_sort_list, 'totals_sort_list': totals_sort_list, 'overallFakeCount': overallFakeCount,
               'last_date': last_date, 'feku_list_pred': feku_list_pred, 'feku_list_RT': feku_list_RT}

    return render(request,'frontend/dashboard_index.html',context)


def trace_1(request):
    top_10_feku_pred, top_10_feku_RT = getIndiaTopFakers()
    int_lst = np.arange(1, 8)
    feku_list_RT = []
    for feku in top_10_feku_RT:
        feku_dict = {}
        feku_dict["time"] = feku[0]
        feku_dict["uname"] = feku[1]
        feku_dict["tweet"] = feku[2]
        feku_dict["label"] = feku[3]
        feku_dict["RT"] = feku[4]
        feku_dict["src"] = "https://bootdey.com/img/Content/avatar/avatar" + str(
            random.choices(int_lst, k=1)[0]) + ".png"
        feku_list_RT.append(feku_dict)
    context = {'feku_list_RT': feku_list_RT}
    return render(request, 'frontend/trace_1.html', context)

def get_city_df():
    lab_lst = ['real', 'fake']
    base_df_city = pd.read_csv('/home/shivam/Downloads/delhi_result.csv')
    N = len(base_df_city)
    df1 = base_df_city
    df1['label'] = random.choices(lab_lst, weights=(0.7, 0.3), k=N)
    hour_list = df1['date'].transform(lambda x: dateutil.parser.parse(x).hour).tolist()
    day_list = df1['date'].transform(lambda x: dateutil.parser.parse(x).day).tolist()
    month_list = df1['date'].transform(lambda x: dateutil.parser.parse(x).month).tolist()
    year_list = df1['date'].transform(lambda x: dateutil.parser.parse(x).year).tolist()
    df1['hour'] = hour_list
    df1['day'] = day_list
    df1['month'] = month_list
    df1['year'] = year_list
    randomproblist = []
    for i in range(0, len(base_df_city)):
        n = np.round(random.uniform(0, 1), 2)
        randomproblist.append(n)
    df1['prob'] = randomproblist

    # Creating a list of retweet values for the given dataframe
    # half will be 0; remaining will be numbers
    # print(f"Total {N}")

    zeros = np.zeros(N // 2).tolist()
    # print(f"Zeros: {len(zeros)}")
    int_lst = np.arange(1, 21)
    # print(int_lst)
    rt_list = random.choices(int_lst, k=(N - N // 2))
    # print(f"RT List: {len(rt_list)}")
    new_rt_list = zeros + rt_list
    random.shuffle(new_rt_list)
    random.shuffle(new_rt_list)
    new_rt_list = [int(x) for x in new_rt_list]
    # print(new_rt_list[:20])
    df1['RT'] = new_rt_list
    return df1


def getIndiaTopFakers():
    df1 = get_city_df()
    top_10_feku_pred = df1[df1['label']=='fake'][['date', 'username', 'tweet', 'label', 'prob']].sort_values(by='prob', ascending=False)[:10].values.tolist()
    top_10_feku_RT = df1[df1['label'] == 'fake'][['date', 'username', 'tweet', 'label', 'RT']].sort_values(by='RT', ascending=False)[:10].values.tolist()
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


def drillDownAState(request):
    print (request.POST.dict())
    # Line chart data for Indian scenario
    stateName=request.POST.get('stateName')
    df1 = get_city_df()
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
    sHist_df = pd.read_csv('statewise_180days_fake_india.csv', index_col=[0])
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
    print("==========>Pritning URI in F2")
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

def frame_4_blank(request, cnt):
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
    context = {'proc_status': False, 'first_disp': True}
    return render(request, 'frontend/frame_4_blank.html', context)
# Location INDEPENDENT (for demo pusposes) frame 4 display
def frame_4(request):
    loc = 'DLI'
    context = {'loc': loc, 'proc_status': True, 'first_disp': False}
    # print("The data is:")
    # print(l2_Data)
    return render(request, 'frontend/frame_4.html', context)
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
            f_obj2 = UploadFileForm()
            response = {'f1': 0, 'f2': 0, 'f3': 0, 'f4': 0, 'f5': 0, 'form1': f_obj1, 'form2': f_obj2, 'loc': loc, 'first_disp': False, 'loc_flag': loc_set}
            return render(request, 'frontend/prediction_V2_V0_First.html', response)
        loc_set=True
        f_obj1 = locationForm(request.POST)
        f_obj2 = UploadFileForm(request.POST, request.FILES)
        # print("=============>File Name", request.POST.get('file', False))
        f_len = len(request.POST.get('file', False))
        loc = request.POST.get('location')
        if f_obj2.is_valid():
            print("File form is totally valid!")
            if f_len!=0 and loc=='OTR':
                loc = 'DEMO'
                print('location set to DEMO')
            else:
                print('Location stays the same')
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
        response = {'f1': 1, 'f2': 1, 'f3': 1, 'f4': 1, 'f5': 1,
                    'form1': f_obj1, 'form2': f_obj2, 'uri': uri, 'loc_flag': loc_set,
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


# On button click backend module to be called, for each tweet in stream and check
@api_view(['GET'])
def contact_F2B_CLS(request, in_text):
    print(request.GET)
    # print(request.POST)
    print("=========*Backend functionality (CLS) accessed! Success*======", str.replace(in_text, '%20', ' '))
    # Logic for Fake news detection/entailment
    # -------Result_class = get_classification_results()
    # -------Result_ent = get_entailment_results()

    Result = FrontendConfig.text_FNF_classify(in_text)
    # out_list = ["URL1", "URL2", "URL3", "URL4", "URL5", "URL6", "URL7", "URL8", "URL9","URL10"]
    Res_Json = {'Tweet': in_text, 'Result': Result}
    return Response(Res_Json)


@api_view(['GET'])
def contact_F2B_ENT(request, in_text):
    print(request.GET)
    # print(request.POST)
    print("=========*Backend functionality (ENT) accessed! Success*======", str.replace(in_text, '%20', ' '))
    # Logic for Fake news detection/entailment
    # -------Result_class = get_classification_results()
    # -------Result_ent = get_entailment_results()
    Result = PredictorConfig.fake_verdict(in_text)
    print(f"==========>Returned updated final entailment verdict: {Result}")
    # out_list = Result[2:]
    # Res_Json = {'Tweet': in_text, 'Result': Result[0], 'o_lst': out_list}
    # Res_Json = {'Tweet': in_text, 'Result': Result, 'o_lst': out_list}
    return Response(Result)
