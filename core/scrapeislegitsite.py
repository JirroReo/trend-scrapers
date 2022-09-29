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

URL = 'https://www.islegitsite.com/recent-checks/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('li', {'class': 'list-group-item'})
count = 0

for r in results:
  title = r.find(attrs={'class': None})
  print(title.text + ' FLAGGED')
  f.write('{}\n'.format(title.text))
  count += 1

print(str(count) + ' links caught!')
f.close()
links = url.processLinks()

data = []
print('Forming data to write')
header = ['Date_Submitted', 'Submitter', 'Source', 'Domain/URL', 'Type']
buf = ''
for link in links:
  data.append([datetime.datetime.now().strftime("%d/%m/%Y"), 'JirroDaveR', 'reverse_tmms-islegitsite', link, 'Financial Scam'])
  buf += '{}\t{}\t{}\t{}\t{}\n'.format(datetime.datetime.now().strftime("%d/%m/%Y"), 'JirroDaveR', 'reverse_tmms-islegitsite', link, 'Financial Scam')

pyperclip.copy(buf)
print('Copied formatted csv to clipboard!')
fname = '{}_islegitsite.csv'.format(datetime.datetime.now().strftime("%d%m%Y"))
print('Writing to {}'.format(fname))
with open('files/{}'.format(fname), 'w', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(header)
  for d in data:
    writer.writerow(d)
print('Success')