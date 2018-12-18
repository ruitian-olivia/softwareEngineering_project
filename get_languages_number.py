import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import matplotlib.pyplot as plt

with open('github_topic.csv',encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    column=[row[0] for row in reader]
topics = column[1:]

dic = {}
for topic in topics:
    URL = "https://github.com/topics/" + topic.lower().replace(" ","-").replace(".","")
    #print(URL)
    r = requests.get(URL)
    soup = BeautifulSoup(r.text)
    #print(soup.select("span"))
    for i in soup.select("span.select-menu-item-text.flex-justify-between"):
        name = str(i).split("\n")[1].strip()
        if name=="All":
            continue
        number = int(str(i).split("\n")[2].split(">")[1].split("<")[0].replace(",",""))
        if dic.get(name) == None:
            dic[name] = number
        else:
            dic[name] += number

def createDictCSV(fileName="", dataDict={}):
    with open(fileName, "w") as csvFile:
        csvWriter = csv.writer(csvFile)
        for k,v in dataDict.items():
            csvWriter.writerow([k,v])
        csvFile.close()

createDictCSV("./language.csv",dic)
