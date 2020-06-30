from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import json
import re
from json import dumps
from urllib.parse import parse_qs

source = requests.get('https://www.google.com/search?q=how to make money online').text

soup = BeautifulSoup(source, 'lxml')
# Crawl result on first page of google and organize
result = []
for link in soup.find_all('a'):
    strWithUrl = link.get('href')
    if re.search('https', strWithUrl):
        if re.search('google', strWithUrl) or re.search('youtube', strWithUrl):
            print('')
        else:
            splittedUrl = strWithUrl.split('?')
            jsonUrl = dumps(parse_qs(splittedUrl[1]))
            resultJSON = json.loads(jsonUrl)
            if 'q' in resultJSON:
                result.append(resultJSON['q'][0])
result = list(dict.fromkeys(result))
print(result)
print(len(result))

# Crawl each of the website
for url in result:
    print('------------------------------------------')
    print('------------------------------------------')
    print(url)
    webData = requests.get(url).text
    soup2 = BeautifulSoup(webData, 'lxml')
    if soup2.article is not None:
        print(soup2.article.get_text())   
    elif ( soup2.find(id="post") is not None ):
        print(soup2.find(id="post"))
    elif ( soup.find_all("div", class_="elementor-widget-wrap") is not None ):
        print(soup.find_all("div", class_="elementor-widget-wrap"))
    else:
        print('Skiiping')