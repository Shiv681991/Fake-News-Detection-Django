import os
import pandas as pd
import tweepy
import time
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor, as_completed
from preprocessor import api
import concurrent
import concurrent.futures


#Twitter credentials for the app
consumer_key = 'Vw1I28kAqmtlR6bxxWC4XRotQ'
consumer_secret = '5BWJpsp7I7flL7A2s6UHKbfkc1CNcJun0oTcBQLpbbAYf5bLux'
access_key= '2457738439-exMpEGlgXiCGMIkdPZ55UzjYZnTDUMWQjJGo6at'
access_secret = 'AYG1URNodgVYONyCXyIgsPBiuwWRLCzy7D29WO0kRNFQE'

#pass twitter credentials to tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# location_dict = {
# "Amritsar": "31.63,74.87,50km",
# "SriNagar": "34.10,74.81,50km",
# "Chandigadh": "30.73,76.76,50km",
# "Delhi": "28.66,77.11,50km",
# "Lucknow": "26.85,80.94,50km",
# "Varanasi": "25.32,82.99,50km",
# "Jaipur": "26.88,75.80,50km",
# "Ahmedabad": "23.02,72.56,50km",
# "Kanpur": "26.45,80.31,50km",
# "Indore": "22.73,75.87,50km",
# "Kolkata": "22.60,88.40,50km",
# "Ranchi": "23.35,85.32,50km",
# "Pune": "18.51,73.86,50km",
# "Mumbai": "19.13,72.89,50km",
# "Guwahati": "26.15,91.74,50km",
# "Hyderabad": "17.42,78.41,50km",
# "Bangalore": "12.94,77.59,50km"}

location_dict = {'Puducherry':"11.94,79.80,100km",
         "Lakshadweep":"10.57,72.64,100km",
         "West_Bengal":"23.00,87.85,100km",
         "Orissa":"20.95,85.09,100km",
         "Bihar":"25.11,85.32,100km",
         "Sikkim":"27.53,87.51,100km",
         "Chattisgarh":"21.30,82.86,100km",
         "TN":"11.12,78.65,100km",
         "MP":"22.97,78.65,100km",
         "Gujrat":"22.25,71.19,100km",
         "Goa":"15.29,74.12,100km",
         "Nagaland":"26.14,96.56,100km",
         "Manipur":"24.44,93.90,100km",
         "Arunachal_Pradesh":"28.00,94.72,100km",
         "Mizoram":"23.20,92.92,100km",
         "Tripura":"23.94,91.98,100km",
         "Daman_and_Diu":"20.39,72.83,50km",
         "Delhi":"28.70,77.12,100km",
         "Haryana":"30.30,74.60,100km",
         "Chandigarh":"30.44,76.47,100km",
         "HP":"31.10,77.17,100km",
         "J&K":"33.27,75.34,100km",
         "Kerela":"10.00,76.25,100km",
         "Karnataka":"15.00,75.00,100km",
         "Dadra_and_Nagar_Haveli":"30.42,76.54,100km",
         "Maharashtra":"20.00,76.00,100km",
         "Assam":"26.00,92.93,100km",
         "AP":"16.00,80.00,100km",
         "Meghalaya":"25.30,91.00,100km",
         "Punjab":"30.40,75.50,100km",
         "Rajasthan":"27.00,74.00,100km",
         "UP":"26.84,80.90,100km",
         "Uttaranchal":"30.15,79.15,100km",
         "Jharkhand":"23.45,85.30,100km"}

cur_city = "Delhi"
pool_size = 5
path = '/home/shivam/PycharmProjects/Django/Django_Warehouse/todo-django-rest-framework-master/todo_drf/statewise_tweets/'
def get_tweets(city_c,city):
    print('yes')
    db = pd.DataFrame(columns=['Tweet_ID', 'username', 'description', 'location', 'following',
                               'followers', 'totaltweets', 'Time_created', 'Likes Count', 'retweetcount', 'text',
                               'hashtags', 'Link'])
    keywords = "#covid19 OR #coronavirus"
    start_date = "2021-02-13"
    result_type = "recent"

    tweets = tweepy.Cursor(api.search, q=keywords + " -filter:retweets",
                           lang="en",geocode=city_c,include_rts=False, tweet_mode='extended').items(1000)
    # while True:
    #     try:
    #         tweet = tweets.next()
    #         # Insert into db
    #         list_tweets.append(tweet)
    #     except tweepy.TweepError:
    #         time.sleep(60 * 15)
    #         continue
    #     except StopIteration:
    #         break
    list_tweets = [tweet for tweet in tweets]

    # Counter to maintain Tweet Count
    i = 1
    url = "https://twitter.com/twitter/statuses/"
    # we will iterate over each tweet in the list for extracting information about each tweet
    for tweet in list_tweets:
        tweet_id = tweet.id_str
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        created_time = tweet.created_at
        favourite_count = tweet.favorite_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']
        link = url+tweet_id

        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])

            # Here we are appending all the extracted information in the DataFrame
        ith_tweet = [tweet_id,username,description, location, following,
                     followers, totaltweets,created_time,favourite_count, retweetcount, text, hashtext,link]
        db.loc[len(db)] = ith_tweet
        i = i + 1
    print(city)
    filename = path+city+'_Tweets'+'.csv'
    db.to_csv(filename)

state_wise = (list(location_dict.values()))

processes = []
with ThreadPoolExecutor(max_workers=10) as executor:
    for city in location_dict:
        processes.append(executor.submit(get_tweets,location_dict[city],city))

for task in as_completed(processes):
    print(task.result())