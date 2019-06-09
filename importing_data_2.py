import requests
from bs4 import BeautifulSoup
import pandas as pd
link_data = []
d = {}
url = 'https://en.wikipedia.org/wiki/Samuel_L._Jackson'
r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc)
print(soup.title)

print(type(soup))

a_tags = soup.find_all('a')

for link in a_tags:
   link_data.append(link.get('href'))

   
def count_entries(list1):
    counts_dict={}

    for entry in list1:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1
    return counts_dict

d = count_entries(link_data)
for key, val in d.items():
    print(str(val) + ' ' +str(val))


##import json
##
##with open('example_1.json') as json_file:
##    json_data = json.load(json_file)
##
##    for key, val in json_data.items():
##        print(key + ': ' + val)
##



##import requests
##imports json
##
##url = ''


























