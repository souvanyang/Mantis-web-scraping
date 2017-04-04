import re
import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup

url = "https://www.federalregister.gov"
urlpath = "https://www.federalregister.gov/agencies/centers-for-medicare-medicaid-services" #url + "/agencies/health-and-human-services-department"
geturl = requests.get(urlpath)
# data = geturl.text
somecontents = geturl.content
soup = BeautifulSoup(somecontents, "html.parser")
soup.prettify()

#time of day
datetime = u'%s' % datetime.today()
print (datetime)

#header title
website_header_title = soup.title.string
print (website_header_title)

#get text
########################### can use this to grab every text
########################### will have to work with parsing with this approach
print (soup.get_text())

#listed below links are childerns of this tag
grab_tag = soup.find_all("div", attrs={"class": "document-wrapper"})

# anchor tags for finding the Article Title
#article_title = soup.find_all("h5")
#findingall = soup.find_all("a")

#anchor tags for finding the Author and Date
#author_date = soup.find_all("p", {"class": "metadata"})

#anchor tags for finding the Description
#article_desc = soup.find_all("p", {"class": "description"})


############# to select specific tags and elements #######
# for i in grab_tag:
# 	try:
# 		print ("Title:" + i.contents[1].find('a').text)
# 	except:
# 		pass
# 	try:
# 		print ("Document number:" + i.contents[3].get("data-document-number"))
# 	except:
# 		pass
# 	try:
# 		print ("by the " + i.contents[5].find('a').text)
# 	except:
# 		pass
# 		print ("\n")
# 	try:
# 		print ("General Description:" + i.contents[7].text)
# 	except:
# 		pass
# 		print ("\n")
