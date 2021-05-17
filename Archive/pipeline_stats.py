# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 10:01:34 2021

@author: AD20168019
"""

"""
Created on Mon Apr  5 10:01:34 2021

@author: AD20168019
"""


import pandas as pd
import numpy as np
from datetime import date, timedelta,datetime
import glob
import os
from random import *
import sys

sys.path.append('/home/shivam/PycharmProjects/Django/Django_Warehouse/todo-django-rest-framework-master/todo_drf')

from frontend import FrontendConfig



def get_verdict(text):
    # print(text)
    out, prob_val = FrontendConfig.text_FNF_classify("This is a sample text")
    # print(state, np.round(prob,2))
    prob = np.round(prob_val, 2)
    # sys.exit()
    # choice = ['fake','real']
    # state = sample(choice,1)
    # if(state == 'fake'):
    #     prob = uniform(0,0.5)
    # else:
    #     prob = uniform(0.5,1)
    return out,prob




os.chdir('/home/shivam/PycharmProjects/Django/Django_Warehouse/todo-django-rest-framework-master/todo_drf/statewise_tweets')
dir_list = glob.glob("*.csv")
file_list = glob.glob('/home/shivam/PycharmProjects/Django/Django_Warehouse/todo-django-rest-framework-master/todo_drf/statewise_tweets/*_Tweets.csv')
#print(dir_list)
state_list = [state.split('_')[0] for state in dir_list]

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


state_list = list(s_Code.values())
code_list = list(s_Code.keys())

df1 = pd.DataFrame()
date_col=[]


for index in range(0,len(state_list)):
    state_code = code_list[index]
    file = state_list[index]+'_Tweets.csv'
    df = pd.read_csv(file)
    df['Verdict']=""
    df['Prob']=""
    #state_name = state_list[index]
    print(file)
    for i in range(0,len(df['text'])):
        x,y = get_verdict(df['text'][i])
        df['Verdict'][i]=x
        df['Prob'][i]=y



    if(not (df.empty)):

        #mindate = (df.date.min())
        #maxdate = (df.date.max())
        mindate = (df.Time_created.min())
        maxdate = (df.Time_created.max())
        #sdate = datetime.strptime(mindate, '%d-%m-%Y %H:%M:%S').date()
        sdate = datetime.strptime(mindate,'%Y-%m-%d %H:%M:%S').date()
        #sdate = datetime.strptime(mindate,'%Y-%m-%d %H:%M:%S%z').date()
        #edate = datetime.strptime(maxdate,'%Y-%m-%d %H:%M:%S%z').date()
        edate = datetime.strptime(maxdate, '%Y-%m-%d %H:%M:%S').date()
        #edate = datetime.strptime(maxdate, '%d-%m-%Y %H:%M:%S').date()


        delta = edate - sdate       # as timedelta
        date_list= []
        for i in range(delta.days + 1):
            day = sdate + timedelta(days=i)
            date_list.append((day))
        #date_list = date_list[::-1]


        for date in date_list:
            if date not in date_col:
                date_col.append(date)
        date_col.sort()


    if(df1.empty):
        df1 = pd.DataFrame(columns =date_col)
        df1.insert(loc=0, column='country_code', value=code_list)
        df1 = df1.set_index('country_code')
        df1 = df1.replace(np.nan,0)

        for i in range(0,len(df)):
            if(df['Verdict'][i]=='fake'):
                #print("yes")
                #date = datetime.strptime(df['date'][i], '%Y-%m-%d %H:%M:%S%z').date()
                date = datetime.strptime(df['Time_created'][i],'%Y-%m-%d %H:%M:%S').date()
                df1[date][state_code] = df1[date][state_code] + 1
    else:
        df1 = df1.reindex(columns=date_col)
        df1 = df1.replace(np.nan,0)
        for i in range(0,len(df)):
            if(df['Verdict'][i]=='fake'):
                #print("yes")
                #date = datetime.strptime(df['date'][i],'%Y-%m-%d %H:%M:%S%z').date()
                date = datetime.strptime(df['Time_created'][i], '%Y-%m-%d %H:%M:%S').date()
                df1[date][state_code] = df1[date][state_code] + 1

df1.reset_index(level=0, inplace=True)
df1.to_csv('stat_numbers_scraped.csv')



file_list = glob.glob('/home/shivam/PycharmProjects/Django/Django_Warehouse/todo-django-rest-framework-master/todo_drf/statewise_tweets/*.csv')
#print(dir_list)
state_list = [state.split('_')[0] for state in dir_list]

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


state_list = list(s_Code.values())
code_list = list(s_Code.keys())

df1 = pd.DataFrame()
date_col=[]


for index in range(0,len(state_list)):
    state_code = code_list[index]
    file = state_list[index]+'_Tweets.csv'
    df = pd.read_csv(file)
    df['Verdict']=""
    df['Prob']=""
    #state_name = state_list[index]
    print(file)
    for i in range(0,len(df['text'])):
        x,y = get_verdict(df['text'][i])
        df['Verdict'][i]=x
        df['Prob'][i]=y
        
        
        
    if(not (df.empty)):
        
        #mindate = (df.date.min())
        #maxdate = (df.date.max())
        mindate = (df.Time_created.min())
        maxdate = (df.Time_created.max())
        #sdate = datetime.strptime(mindate, '%d-%m-%Y %H:%M:%S').date()
        sdate = datetime.strptime(mindate,'%Y-%m-%d %H:%M:%S').date()
        #sdate = datetime.strptime(mindate,'%Y-%m-%d %H:%M:%S%z').date()
        #edate = datetime.strptime(maxdate,'%Y-%m-%d %H:%M:%S%z').date()
        edate = datetime.strptime(maxdate, '%Y-%m-%d %H:%M:%S').date()
        #edate = datetime.strptime(maxdate, '%d-%m-%Y %H:%M:%S').date()
        
        
        delta = edate - sdate       # as timedelta
        date_list= []
        for i in range(delta.days + 1):
            day = sdate + timedelta(days=i)
            date_list.append((day))
        #date_list = date_list[::-1]
        
        
        for date in date_list:
            if date not in date_col:
                date_col.append(date)
        date_col.sort()
    
    
    if(df1.empty):
        df1 = pd.DataFrame(columns =date_col)
        df1.insert(loc=0, column='country_code', value=code_list)
        df1 = df1.set_index('country_code')
        df1 = df1.replace(np.nan,0)
        
        for i in range(0,len(df)):
            if(df['Verdict'][i]=='fake'):
                #print("yes")
                #date = datetime.strptime(df['date'][i], '%Y-%m-%d %H:%M:%S%z').date()
                date = datetime.strptime(df['Time_created'][i],'%Y-%m-%d %H:%M:%S').date()
                df1[date][state_code] = df1[date][state_code] + 1
    else:
        df1 = df1.reindex(columns=date_col)
        df1 = df1.replace(np.nan,0)
        for i in range(0,len(df)):
            if(df['Verdict'][i]=='fake'):
                #print("yes")
                #date = datetime.strptime(df['date'][i],'%Y-%m-%d %H:%M:%S%z').date()
                date = datetime.strptime(df['Time_created'][i], '%Y-%m-%d %H:%M:%S').date()
                df1[date][state_code] = df1[date][state_code] + 1

df1.reset_index(level=0, inplace=True)
df1.to_csv('stat_numbers_scraped.csv')

    
    