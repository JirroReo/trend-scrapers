# ---------------------------------------------------------------------------------------------------------------------------------------------
# Code written by
# Jirro Dave Reoloso (TR-PH-INTRN as of September 8, 2022)
# ---------------------------------------------------------------------------------------------------------------------------------------------


import requests
import subprocess
import url
import datetime
import pyperclip
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

f = open('input.txt', 'w')
f.write('')
f.close()

f = open('input.txt', 'a')

URL = 'https://scammer.info/latest'
options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Edge(options=options)
driver.get(URL)

for i in range(0,10): # here you will need to tune to see exactly how many scrolls you need
    driver.execute_script('window.scrollBy(0, 2000)')
    time.sleep(1)

all = driver.find_elements(By.CSS_SELECTOR, "a.title.raw-link.raw-topic-link")
links = []
count = 0
for a in all:
  # print(a.text)
  try:
    payload = re.search('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', a.text).group(1)
    if payload: 
      print(payload)
      links.append(payload)
      f.write('{}\n'.format(payload))
      count += 1
  except AttributeError:
    pass

print('\n{} numbers captured!'.format(count))
f.close()
driver.quit()

data = []
print('Forming data to write')
header = ['Date Added', 'Submitter', 'Source', 'Telephone', 'Email Address', 'Scam Type']
buf = ''
for link in links:
  data.append([datetime.datetime.now().strftime("%d/%m/%Y"), 'JirroDaveR', 'scammerinfo', link, '', 'Tech Support Scam'])
  buf += '{}\t{}\t{}\t{}\t{}\t{}\n'.format(datetime.datetime.now().strftime("%d/%m/%Y"), 'JirroDaveR', 'scammerinfo', link, '', 'Tech Support Scam')

pyperclip.copy(buf)
print('Copied formatted csv to clipboard!')
fname = '{}_scammerinfo.csv'.format(datetime.datetime.now().strftime("%d%m%Y"))
print('Writing to {}'.format(fname))
with open('files/{}'.format(fname), 'w', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(header)
  for d in data:
    writer.writerow(d)
print('Success')