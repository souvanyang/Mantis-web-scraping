import re
import requests
import json
import urllib
#import xml.dom.minidom
from datetime import datetime
from bs4 import BeautifulSoup
url = input('What URL do you want to go to? :')
#grab URL
def grab_url(myurl):
    # grab content
    geturl = requests.get(myurl)
    # data = geturl.text
    somecontents = geturl.content
    soup = BeautifulSoup(somecontents, "html.parser")
    soup.prettify()
    # title website
    website_header_title = soup.title.string
    print (website_header_title)
    print (soup.get_text())

grab_url(url)
# grab content
