import json
import re
import requests
import json
import sys
import os
import csv
from datetime import datetime
from bs4 import BeautifulSoup

url = "https://www.federalregister.gov"
urlpath = url + "/agencies/health-and-human-services-department"
geturl = requests.get(urlpath)
data = geturl.text
somecontents = geturl.content
datetime = u'%s' % datetime.today()
# print (datetime)
soup = BeautifulSoup(somecontents, "html.parser")
soup.prettify()
links = soup.find_all("div", attrs={"class": "document-wrapper"})

try:
    for i in links:
        data = {}
        data['Articles'] = []
        data['Articles'].append({
            'Date' : datetime,
            'Title' : i.contents[1].find('a').text,
    	    'Document number' : i.contents[3].get("data-document-number"),
    		'by the' : i.contents[5].find('a').text
        #    'General Description' : i.contents[7].text
        })
        data['Description'].append({
            'General Description' : i.contents[7].text
        })
except:
    pass

    with open('testsouvan.json', 'w') as outfile:
        json.dump(data, outfile)

# data = {}
# data['article'] = []
# data['article'].append({
#     soup.find_all("div", attrs={"class": "document-wrapper"}),
#     soup.find_all("p", {"class": "metadata"}),
#     soup.find_all("p", {"class": "description"})
# })
# data['people'].append({
#     'name': 'Larry',
#     'website': 'google.com',
#     'from': 'Michigan'
# })
# data['people'].append({
#     'name': 'Tim',
#     'website': 'apple.com',
#     'from': 'Alabama'
# })
