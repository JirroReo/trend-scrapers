# ---------------------------------------------------------------------------------------------------------------------------------------------
# Code written by
# Jirro Dave Reoloso (TR-PH-INTRN as of September 8, 2022)
# ---------------------------------------------------------------------------------------------------------------------------------------------

import url
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import pyperclip
import csv


f = open('input.txt', 'w')
f.write('')
f.close()

f = open('input.txt', 'a')
URL = 'https://scamscavenger.tech/'

options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Edge(options=options)
driver.get(URL)

count = 0
all = driver.find_elements(By.CSS_SELECTOR, "h4.trial-rating")

del all[-1]
del all[-1]

for a in all:
  print(a.text, end='\n')
  f.write('{}\n'.format(a.text))
  count += 1

print('\n{} links caught!'.format(count))
f.close()
driver.quit()


links = url.processLinks()
data = []
print('Forming data to write')
header = ['Date_Submitted', 'Submitter', 'Source', 'Domain/URL', 'Type']
buf = ''
for link in links:
  data.append([datetime.datetime.now().strftime("%d/%m/%Y"), 'JirroDaveR', 'reverse_tmms-scamscavenger', link, 'Cryptocurrency Scam'])
  buf += '{}\t{}\t{}\t{}\t{}\n'.format(datetime.datetime.now().strftime("%d/%m/%Y"), 'JirroDaveR', 'reverse_tmms-scamscavenger', link, 'Cryptocurrency Scam')

pyperclip.copy(buf)
print('Copied formatted csv to clipboard!')
fname = '{}_scamscavenger.csv'.format(datetime.datetime.now().strftime("%d%m%Y"))
print('Writing to {}'.format(fname))
with open('files/{}'.format(fname), 'w', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(header)
  for d in data:
    writer.writerow(d)
print('Success')