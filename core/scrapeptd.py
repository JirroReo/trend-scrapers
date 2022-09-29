# ---------------------------------------------------------------------------------------------------------------------------------------------
# Code written by
# Jirro Dave Reoloso (TR-PH-INTRN as of September 8, 2022)
# ---------------------------------------------------------------------------------------------------------------------------------------------


import requests
import subprocess
import url
from bs4 import BeautifulSoup
import csv
import datetime
import pyperclip

f = open('input.txt', 'w')
f.write('')
f.close()

f = open('input.txt', 'a')
count = 0
for pagenum in range(1, 11):
  URL = 'https://preventingtruthdecay.org/?scam={}'.format(pagenum)
  page = requests.get(URL)

  soup = BeautifulSoup(page.content, 'html.parser')
  results = soup.find_all('div', {'class': 'title'})

  for r in results:
    print(r.text, end='\n')
    count += 1
    f.write('{}\n'.format(r.text))

print(str(count) + ' links caught!')
f.close()
links = url.processLinks()

data = []
print('Forming data to write')
header = ['Date_Submitted', 'Submitter', 'Source', 'Domain/URL', 'Type']
buf = ''
for link in links:
  data.append([datetime.datetime.now().strftime("%d/%m/%Y"), 'JirroDaveR', 'preventingtruthdecay', link, 'Shopping Scam'])
  buf += '{}\t{}\t{}\t{}\t{}\n'.format(datetime.datetime.now().strftime("%d/%m/%Y"), 'JirroDaveR', 'preventingtruthdecay', link, 'Shopping Scam')

pyperclip.copy(buf)
print('Copied formatted csv to clipboard!')
fname = '{}_ptd.csv'.format(datetime.datetime.now().strftime("%d%m%Y"))
print('Writing to {}'.format(fname))
with open('files/{}'.format(fname), 'w', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(header)
  for d in data:
    writer.writerow(d)
print('Success')