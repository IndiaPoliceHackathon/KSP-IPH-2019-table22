"""from urllib.request import urlopen
from bs4 import BeautifulSoup
def getNews(url):
    html = urlopen('https://timesofindia.indiatimes.com{}'.format(url))
    bs4 = BeautifulSoup(html, 'html.parser')
    for link in bs4.find('div', {'class':'top-story'}).find_all('a'):
        print(link.get_text())
        if 'href' in link.attrs:
                html_i = urlopen('https://timesofindia.indiatimes.com'+link.attrs['href'])
                bs = BeautifulSoup(html_i, 'html.parser')
                print('\t' + bs.find('artsummary').find('ul').find('li').get_text())
getNews('')"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
def getNews(url):
    html = urlopen('https://timesofindia.indiatimes.com{}'.format(url))
    bs4 = BeautifulSoup(html, 'html.parser')
    for link in bs4.find('div', {'class':'top-story'}).find_all('a'):
        print(link.get_text())
        if 'href' in link.attrs:
                html_i = urlopen('https://timesofindia.indiatimes.com'+link.attrs['href'])
                bs = BeautifulSoup(html_i, 'html.parser')
                print('\t' + bs.find('artsummary').get_text())
getNews('')