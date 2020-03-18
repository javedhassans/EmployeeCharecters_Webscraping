# Importing Dependecies
from bs4 import BeautifulSoup
import urllib3
import pandas as pd
import time

# %%

starttime = time.time()
# Creating the initial hit with the initial page url
http = urllib3.PoolManager()
url = "https://news.tabularazor.org/2012.html"
response = http.request('GET', url)
# print("The hit is the success as the code is ", response.status)
# using the parser for the
soup = BeautifulSoup(response.data, features="html.parser")
list_0 = []
list_0_1 = []
for link in soup.find_all('a'):
    list_0.append(link.get('href'))
for i in list_0:
    list_0_1.append("https://news.tabularazor.org" + i)  # this converts obtained links to urls
# print(list_0_1)
# optional if you want to save teh output file for verification
# with open('file_01.html', "w", encoding="utf-8") as f:
#     f.write(str(soup))

# %%
# preparing the urls for fetching further urls
list_1 = []
list_1_1 = []
for i in list_0_1:
    # print(i)
    # hitting the fetched urls from the above step
    response1 = http.request('GET', str(i))
    # print(response1.data)
    soup1 = BeautifulSoup(response1.data, features="html.parser")
    # print(soup1)

    for a in soup1.find_all('a'):
        list_1.append(a.get('href'))
        # print(list_1)
    for i in list_1:
        list_1_1.append("https://news.tabularazor.org" + i)  # this converts obtained links to urls
        # print(list_1_1)

# optional if you want to save it for verification
# with open('file_02.html', "a+", encoding="utf-8") as f:
#     f.write(str(soup1))


# %%
list_1_1[:5]

# %%
# hitting the final page and extracting the required details
title = []
date = []
hours = []
author = []
for i in list_1_1[:5]:
    # print(i)
    response2 = http.request('GET', str(i))
    # print(response2.data)
    soup2 = BeautifulSoup(response2.data, features="html.parser")
    # print(soup2)

    names = soup2.find('div', attrs={"class": "author"})
    dates = soup2.find('div', attrs={"class": "date"})
    times = soup2.find('div', attrs={"class": "time"})
    titles = soup2.find('title')

    title.append(titles.text)
    author.append(names.text)
    hours.append(times.text)
    date.append(dates.text)

# this is optional if you want to save the file
# with open('file_03.html', "a+", encoding="utf-8") as f:
#     f.write(str(soup2))

# print(author)
# print(title)
# print(date)
# print(hours)


# %%

df = pd.DataFrame({'author': author, "title": title, "date": date, "time": time})
print(df.info())
df.to_csv("assaign03.csv")
