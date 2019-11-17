from bs4 import BeautifulSoup as soup
import pandas as pd
from urllib.request import urlopen as uReq
url="https://www.ndtv.com/latest"
p=open("news.txt","w+")
print(p)

r1 = requests.get(url)
print(r1.status_code)

# We'll save in coverpage the cover page content
coverpage = r1.content

# Soup creation
soup1 = soup(coverpage, 'html5lib')
news_div = soup1.findAll("div",{"class":"nstory_header"})
news_story = soup1.findAll("div",{"class":"nstory_intro"})

# News identification
print(len(news_div))
urls=[]
for i in range(len(news_div)):
    p.write(news_div[i].text)
    p.write(news_story[i].text)
    print(news_div[i].text)
    print(news_story[i].text)
    
    print(news_div[i].a['href'])
    urls.append(news_div[i].a['href'])

print(urls)



    