"""
" This program is used for parsing RSS news feed of each quote
" from source 'http://articlefeeds.nasdaq.com/nasdaq/symbols?symbol=[quote]'
"""

import datetime
import feedparser
import csv
import sys
import os

# Check existance of destination directory
directory = 'source'
if not os.path.exists(directory):
    os.makedirs(directory)
# Receive input
quote_symbol = str(sys.argv[1].upper())
# Create a variable with the feed's URL
feed_url = 'http://articlefeeds.nasdaq.com/nasdaq/symbols?symbol='+quote_symbol

print('Receiving Feed for '+quote_symbol)
# Parse feed at the url
feed = feedparser.parse(feed_url)

list_of_news = []
for post in feed.entries:
    list_of_vals = []
    pub_date = datetime.datetime.strptime(post.published, '%a, %d %b %Y %H:%M:%S Z').strftime('%m/%d/%Y')
    list_of_vals.append(pub_date)
    list_of_vals.append(quote_symbol)
    list_of_vals.append(post.title)
    list_of_vals.append(post.description)
    list_of_news.append(list_of_vals)

file_path = "./source/news_"+quote_symbol.lower()+".csv"
directory = os.path.dirname(file_path)
if not os.path.exists(directory):
    os.makedirs(directory)
with open(file_path, "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Date","Symbol","Title","Description"])
    writer.writerows(list_of_news)

print ('Parsing news feed for '+quote_symbol+' is completed.')
