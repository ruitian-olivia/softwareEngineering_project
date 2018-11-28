import requests
from bs4 import BeautifulSoup
import pandas as pd

path = './topic.html'
with open(path, 'r',encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(),"lxml")
    
topic = soup.find_all(class_="py-4 border-bottom")
topicName = []
topicAbstract = []
for i in topic:
    Name = i.find("p").contents
    Abstract = i.find("p").next_sibling.next_sibling.contents
    topicName.append(Name[0])
    topicAbstract.append(Abstract[0])
    
hotDF = pd.DataFrame()
hotDF['Topic'] = topicName
hotDF['Abstract'] = topicAbstract
hotDF.to_csv('./github_topic.csv', index=False)
