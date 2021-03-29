import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
import sys, time
import random
from googlesearch import search
from datetime import datetime

def content_extraction_from_tweet(query, domain):
    # query = "Trump touting #Hydroxychloroquine as a cure for #COVIDー19 was BAD enough.We will NEVER forget Trump said if you are on HCQ &amp; you have Lupus, you can't get #coronavirus Thanks to Trump there is now a SHORTAGE.I &amp; many are RATIONING our medication."
    url_list=[]
    url_extracted=[]
    webcontent=[]
    headline_list=[]
    wt = random.uniform(10, 20)
    print("------------------------")
    print("Pre-search...")
    for j in search(query, lang='en', tld=domain, num=60, stop=60, pause=wt):
        print(j)
        url_list.append(j)
    print("------------------------")
    print("Post-search...")

    cur_name = '_'.join(query.split())
    save_file_path = "web_content/Downloaded/webcontent_google_search_"+cur_name+"_"+datetime.now().strftime("%H_%M_%S")+".csv"
    with open(save_file_path, "w") as x:
        writer = csv.writer(x)
        for i in range(len(url_list)):
            try:
                print("Processing URL...{}/{}".format(i, len(url_list)))
                #url = 'https://web.archive.org/web/20170415165124/http://thenewyorkevening.com:80/2017/04/10/breaking-malia-obama-expelled-harvard'
                res = requests.get(url_list[i])
                html_page = res.content
                soup = BeautifulSoup(html_page, 'html.parser')
                text = soup.find_all(text=True)
                # set([t.parent.name for t in text])
                output = ''
                headline=""
                headline_tags=["h1","title"]
                # headline_tags=["h1"]
                tags = [
                    "p", "span"
                    # there may be more elements you don't want, such as "style", etc.
                ]
                # print("===================")
                # print("Type: ", type(text))
                # print("URL: ", url_list[i])
                # print("Len text: ", len(text))
                # print(text)
                # sys.exit()
                for t in text:
                    if t.parent.name in headline_tags:
                        # print("===========Title tags")
                        # print(t)
                        headline += '{} '.format(t)

                for t in text:
                    if t.parent.name in tags:
                        # print("===========Normal tags")
                        # print(t)
                        if bool(t.strip()) == True and len(t.split()) > 3:
                            if t.split()[0].strip() != "Share":
                                if t.split()[0].strip() != "share":
                                    if t.split()[0].strip() != "Log":
                                        if t.split()[0].strip() != "log":
                                            if t.split()[0].strip() != "Sign":
                                                if t.split()[0].strip() != "sign":
                                                    #                         print("getting t: ",t)
                                                    output += '{} '.format(t)

                #             print("main output: ",output)
                # if bool(output.strip()) == True:

                if bool(output.strip()) == False:
                    output=None
                    webcontent.append(output)
                else:
                    webcontent.append(output)
                if bool(headline.strip()) == False:
                    headline=None
                    headline_list.append(headline)
                else:

                    headline_list.append(headline)
                url_extracted.append(url_list[i])
                writer.writerow([url_list[i],headline, output])
                print("------------------------")
                print("Content saved...{}/{}".format(i, len(url_list)))
            except:
                pass
        print("{} processed.".format(cur_name))
    return url_extracted,headline_list,webcontent

# cat_list = ["Modi", "Kejriwal", "Boris Johnson", "Barack Obama"]
# cat_list = ["Katy Perry", "Taylor Swift", "Shakira"]
# # "Donald Trump"
# while True:
#     for cat in cat_list:
#         print("------------------------")
#         print("Beginning new search...")
#         TLD = "com"
#         # if cat in ["Boris Johnson", "Barack Obama"]:
#         #     TLD = "com"
#         # elif cat in ["Modi", "Kejriwal"]:
#         #     TLD = "co.in"
#         query = cat
#         url,title,content=content_extraction_from_tweet(query, TLD)
#         print(url,title,content)
#         time.sleep(60)
# YTD: [Katy Perry, Taylor Swift, Shakira, Barack Obama]
query = "Britney Spears"
TLD="com"
url,title,content=content_extraction_from_tweet(query, TLD)
print(url,title,content)