import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MT.settings")
django.setup()
import bs4
import requests
import time
from ws.models import News
import datefinder
import datetime


"""
************Saving to database******************
date format :YYYY-MM-DD and it should be string
content should be string
title should be string 
************************************************

"""

name_bbc = "bbc"
name_reuters = "reuters"
name_ibt = "IBT"


def latest_business_news_bbc():
    urls = []
    url = 'https://www.bbc.com/news'
    resp = requests.get(url)
    sop = bs4.BeautifulSoup(resp.text, 'html.parser')
    for i in sop.find('div', class_='nw-c-most-read__items').find_all('a'):
        urls.append("http://www.bbc.com" + i.get('href'))
    return urls


def article_content__bbc(url):
    resp = requests.get(url)
    sop = bs4.BeautifulSoup(resp.text, 'html.parser')
    content = []
    article_date_tem = sop.find('div', class_='date').text
    # convert date format into YYYY-MM-DD
    article_date = time.strftime('%Y-%m-%d', time.localtime(time.mktime(time.strptime(article_date_tem, '%d %B %Y'))))
    title = str(sop.find('h1').text)
    p = sop.find('div', property='articleBody')
    for i in p.find_all('p'):
        content.append(str(i))
    return title, article_date, content



def latest_business_news_reuters():
    urls = []
    url_header ="https://www.reuters.com"
    url = "https://www.reuters.com/news/archive/businessNews?view=page"
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    for i in soup.find_all('div', class_='story-content'):
            urls.append(url_header + i.h3.parent.get('href'))
    return urls


def article_content_reuters(url):
    contents = []
    titles = []
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    # find date in text, it can output date in format
    matches = datefinder.find_dates(soup.find('div', class_='date_V9eGk').text)
    for match in matches:
        # convert date format into YYYY-MM-DD
        date = str(datetime.datetime.date(match))
    titles = str(soup.find('div', class_='content-container_3Ma9y').h1.text)
    content = soup.find('div', class_='body_1gnLA')
    for i in content.find_all('p'):
        contents.append(str(i))
    return titles, date, contents


# date format: 2018-06-15


def latest_business_news_ibt():
    urls = []
    url_header = "http://www.ibtimes.com"
    url = "http://www.ibtimes.com/business"
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    for i in soup.find_all('article', class_='clearfix'):
         urls.append(url_header + i.h3.a.get('href'))
    return urls


def article_content_ibt(url):
    contents = []
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    date_ibt = datefinder.find_dates(soup.find('time', itemprop='datePublished').text)
    for i in date_ibt:
        # convert date format into YYYY-MM-DD
        date = str(datetime.datetime.date(i))
    soup_1 = soup.find('div', class_='article-body')
    for content in soup_1.find_all('p'):
        contents.append(str(content))
    titles = str(soup.find('header', class_='article-header').h1.text)
    return titles, date, contents


def save_article_content():
    link_bbc = latest_business_news_bbc()
    link_reuters = latest_business_news_reuters()
    link_ibt = latest_business_news_ibt()
    for i in link_bbc:
        title, article_date, content_bbc = article_content__bbc(i)
        #convert list to string
        contents_bbc = ''.join(str(e) for e in content_bbc)
        News.objects.get_or_create(name=name_bbc, title=title,  date=article_date, content=contents_bbc)
    print("***************BBC Done****************")

    for i in link_reuters:
        title, article_date, content_reuters = article_content_reuters(i)
        contents_reuters = ''.join(str(e) for e in content_reuters)
        News.objects.get_or_create(name=name_reuters, title=title, date=article_date, content=contents_reuters)
    print("***************REUTERS Done****************")

    for i in link_ibt:
        title, article_date, content_ibt = article_content_ibt(i)
        contents_ibt = ''.join(str(e) for e in content_ibt)
        News.objects.get_or_create(name=name_ibt, title=title, date=article_date, content=contents_ibt)
        # get_or_create() can ensure data is unique
    print("***************IBT Done****************")


save_article_content()
print("*************** ALL DONE ****************")
