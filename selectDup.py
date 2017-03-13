"""
This program is used for generate the list of news containing the latest news
from each day before consolidate with news from other quote sumbols
"""

import sys
import csv
from itertools import groupby

quote_symbol = str(sys.argv[1].lower())

in_file = 'source/news_'+quote_symbol+'.csv'
out_file = 'source/distinc_'+quote_symbol+'.csv'

def main():
    with open(in_file, 'r') as inf, open(out_file, 'w', newline='') as outf:
        incsv  = csv.reader(inf)
        outcsv = csv.writer(outf)
        for date,rows in groupby(incsv, key=lambda row: row[0:2]):
            outcsv.writerow(next(rows))

if __name__=="__main__":
    main()
