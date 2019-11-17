from bs4 import BeautifulSoup as soup
import pandas as pd
from urllib.request import urlopen as uReq
url="https://timesofindia.indiatimes.com/topic/crime/news"
s=[str(i) for i in range(2,16)]
print(s)
k=[url+i for i in s]
print(k)

r1 = requests.get(url)
print(r1.status_code)

# We'll save in coverpage the cover page content
coverpage = r1.content

# Soup creation
soup1 = BeautifulSoup(coverpage, 'html5lib')
news_div = soup1.findAll("div",{"class":"content"})


# News identification
print(len(news_div))
urls=[]
for i in range(len(news_div)):
    print(news_div[i].text)
    


for i in range(len(k)):
           r1 = requests.get(k[i])
           if(r1.status_code!=404):
               print(r1.status_code)
            
# We'll save in coverpage the cover page content
               coverpage = r1.content

# Soup creation
               soup1 = BeautifulSoup(coverpage, 'html5lib')
               news_div = soup1.findAll("div",{"class":"content"})


# News identification
               print(len(news_div))

               for i in range(len(news_div)):
                   print(news_div[i].text)