"""
" This program is used for parsing history quote close prices and volumes of
" each symbol on each day from source 'http://www.nasdaq.com/symbol/[quote]/historical'
"""

import requests
import lxml
import csv
from bs4 import BeautifulSoup
import sys 

# Receive input
quote_symbol = str(sys.argv[1].lower())
# Create a variable with the URL
url = 'http://www.nasdaq.com/symbol/'+quote_symbol+'/historical'
# Scrape the HTML at the url
req = requests.get(url)
# Turn the HTML into a Beautiful Soup object
soup = BeautifulSoup(req.text, 'lxml')

print ('Start parsing quote information for '+quote_symbol.upper())
division = soup.find('div', attrs={'id': 'quotes_content_left_pnlAJAX'})
table = division.find('table')

list_of_rows = []
for row in table.find_all('tr') [2:]:
    list_of_cells = []
    cell = row.find_all('td')
    text = cell[0].text.strip()
    list_of_cells.append(text)
    list_of_cells.append(quote_symbol.upper())
    text = cell[4].text.strip()
    list_of_cells.append(text)
    text = cell[5].text.strip()
    list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

with open("./source/historical_"+quote_symbol+".csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Date","Symbol","Close","Volume"])
    writer.writerows(list_of_rows)

print ('Parsing raw quote information for '+quote_symbol.upper()+' is completed.')
