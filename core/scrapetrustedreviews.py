# ---------------------------------------------------------------------------------------------------------------------------------------------
# Code written by
# Jirro Dave Reoloso (TR-PH-INTRN as of September 8, 2022)
# ---------------------------------------------------------------------------------------------------------------------------------------------


import requests
import subprocess
import url
from bs4 import BeautifulSoup
import datetime
import pyperclip
import csv

f = open('input.txt', 'w')
f.write('')
f.close()

f = open('input.txt', 'a')

URL = 'https://trustedrevie.ws/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('div', {'class': 'index-reviews-box'})

logged = []

for r in results:
  name = r.find('a', {'class': 'review-company'})
  name = name.text.strip()
  if r.find('div', {'class': 'rdc-stars-low'}) or r.find('div', {'class': 'rdc-stars-mid'}):
    if not name in logged:
      print(name, end='\n')
      f.write('{}\n'.format(name))
      logged.append(name)

f.close()
links = url.processLinks()

data = []
print('Forming data to write')
header = ['Date_Submitted', 'Submitter', 'Source', 'Domain/URL', 'Type']
buf = ''
for link in links:
  data.append([datetime.datetime.now().strftime("%d/%m/%Y"), 'JirroDaveR', 'trustedreviews', link, 'Financial Scam'])
  buf += '{}\t{}\t{}\t{}\t{}\n'.format(datetime.datetime.now().strftime("%d/%m/%Y"), 'JirroDaveR', 'trustedreviews', link, 'Financial Scam')

pyperclip.copy(buf)
print('Copied formatted csv to clipboard!')
fname = '{}_trustedreviews.csv'.format(datetime.datetime.now().strftime("%d%m%Y"))
print('Writing to {}'.format(fname))
with open('files/{}'.format(fname), 'w', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(header)
  for d in data:
    writer.writerow(d)
print('Success')