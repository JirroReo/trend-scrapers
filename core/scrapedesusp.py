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

dateToday = datetime.date.today()
validDates = [dateToday]
dayOfTheWeek = datetime.datetime.today().weekday() # get what day of the week it is today as an int, 0 = Monday, 6 = Sunday
if dayOfTheWeek == 0: # if today is a monday, we also accept posts from saturday and sunday
  sunday = dateToday - datetime.timedelta(1)
  validDates.append(sunday)
  saturday = sunday - datetime.timedelta(1)
  validDates.append(saturday)

count = 0
for pagenum in range(1, 5):
  print('Scraping page {}...'.format(pagenum))
  invalidFlag = False
  URL = 'https://de-reviews.com/category/suspicious/page/{}/'.format(pagenum)
  page = requests.get(URL)

  soup = BeautifulSoup(page.content, 'html.parser')
  results = soup.find_all('article', {'class': 'post excerpt'})

  for r in results:
    date = r.find('div', {'class': 'post-date-ribbon'})
    articleDate = datetime.datetime.strptime(date.text, '%B %d, %Y').date()

    if articleDate in validDates: # if article is posted in the range of valid dates
      title = r.find('a', {'rel': 'bookmark'})
      title = title.text.split(" Review", 1)[0] # Gets the words before "Review" in the title
      title = title.split(" ") # Convert into list
      if len(title) > 1: # Title has 'shop' 'store' 'online' or anything else in link
        finalURL = '{}.{}'.format(title[0], title[1])
        print(finalURL)
      else:
        finalURL = '{}.com'.format(title[0])
        print(finalURL)

      count += 1
      f.write('{}\n'.format(finalURL))

    else:
      invalidFlag = True # true if we have reached the end of the valid dates
      break

  if invalidFlag: break # if we have reached the end of the valid dates stop going through the pages

print(str(count) + ' links caught!')
f.close()
links = url.processLinks()

data = []
print('Forming data to write')
header = ['Date_Submitted', 'Submitter', 'Source', 'Domain/URL', 'Type']
buf = ''
for link in links:
  data.append([datetime.datetime.now().strftime("%d/%m/%Y"), 'JirroDaveR', 'reverse_tmms-dereviews', link, 'Shopping Scam'])
  buf += '{}\t{}\t{}\t{}\t{}\n'.format(datetime.datetime.now().strftime("%d/%m/%Y"), 'JirroDaveR', 'reverse_tmms-dereviews', link, 'Shopping Scam')

pyperclip.copy(buf)
print('Copied formatted csv to clipboard!')
fname = '{}_desuspicious.csv'.format(datetime.datetime.now().strftime("%d%m%Y"))
print('Writing to {}'.format(fname))
with open('files/{}'.format(fname), 'w', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(header)
  for d in data:
    writer.writerow(d)
print('Success')