import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import matplotlib.pyplot as plt

with open('github_topic.csv',encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    column=[row[0] for row in reader]
topics = column[1:]

for topic in topics:
    URL = "https://github.com/topics/" + topic.lower().replace(" ","-").replace(".","")
    r = requests.get(URL)
    soup = BeautifulSoup(r.text)
    name_list = []
    num_list = []
    for i in soup.select("span.select-menu-item-text.flex-justify-between"):
        name = str(i).split("\n")[1].strip()
        name_list.append(name)
        number = str(i).split("\n")[2].split(">")[1].split("<")[0].replace(",","")
        num_list.append(int(number))
    if name_list == []:
        continue
    plt.barh(range(len(num_list)), num_list,tick_label = name_list,color="powderblue")
    plt.title(topic+" language distribution")
    plt.tight_layout()
    plt.savefig('./topic_languages/'+topic+'_language.png')
    plt.close("all")
