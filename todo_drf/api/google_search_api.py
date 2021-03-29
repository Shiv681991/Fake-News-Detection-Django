import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup

from googlesearch import search

def content_extraction_from_tweet(query):
    # query = "Trump touting #Hydroxychloroquine as a cure for #COVIDー19 was BAD enough.We will NEVER forget Trump said if you are on HCQ &amp; you have Lupus, you can't get #coronavirus Thanks to Trump there is now a SHORTAGE.I &amp; many are RATIONING our medication."
    url_list=[]
    url_extracted=[]
    webcontent=[]
    headline_list=[]
    for j in search(query, tld="com", num=10, stop=10, pause=2):
        print(j)
        url_list.append(j)


    save_file_path = "webcontent_google_search.csv"
    with open(save_file_path, "w") as x:
        writer = csv.writer(x)
        for i in range(len(url_list)):
            try:
                #             url = 'https://web.archive.org/web/20170415165124/http://thenewyorkevening.com:80/2017/04/10/breaking-malia-obama-expelled-harvard'
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
                for t in text:
                    if t.parent.name in headline_tags:
                        headline += '{} '.format(t)

                for t in text:
                    if t.parent.name in tags:
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
            except:
                pass
    return url_extracted,headline_list,webcontent

# query = "Trump touting #Hydroxychloroquine as a cure for #COVIDー19 was BAD enough.We will NEVER forget Trump said if you are on HCQ &amp; you have Lupus, you can't get #coronavirus Thanks to Trump there is now a SHORTAGE.I &amp; many are RATIONING our medication."
# url,title,content=content_extraction_from_tweet(query)
# print(url,title,content)