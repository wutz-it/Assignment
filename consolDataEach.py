"""
' This program is used for consolidate quote information for each requested symbols
' Listed in 'config\config.txt' and consolidate their news in a separate csv
'
"""

import sys
import csv
import os
from itertools import groupby

quote_symbol = str(sys.argv[1].lower())

distinc_in_file = 'source/distinc_'+quote_symbol+'.csv'
historical_in_file = 'source/historical_'+quote_symbol+'.csv'
out_file = 'report/comb_'+quote_symbol+'.csv'
directory = os.path.dirname(out_file)
if not os.path.exists(directory):
    os.makedirs(directory)

def main():
    print ('Combine quotes and news separatedly')
    with open(distinc_in_file, 'r') as distinc_inf, open(historical_in_file, 'r') as historical_inf, open(out_file, 'w', newline='') as outf:
        distinc_incsv  = csv.reader(distinc_inf)
        distinc_in_list = list(distinc_incsv)
        historical_incsv  = csv.reader(historical_inf)
        historical_in_list = list(historical_incsv)
        outcsv = csv.writer(outf)
       
        newlist = []
        
        for quote_column in historical_in_list:
            isFound_news = 0
            key_historical = quote_column[0] + ":" + quote_column[1]
            for news_column in distinc_in_list:
                key_distinc = news_column[0] + ":" + news_column[1]
                if key_historical == key_distinc:
                    temp = []
                    temp.append(quote_column[0])
                    temp.append(quote_column[1])
                    temp.append(quote_column[2])
                    temp.append(quote_column[3])
                    temp.append(news_column[2])
                    temp.append(news_column[3])
                    newlist.append(temp)
                    isFound_news = 1
            if isFound_news == 0:
                temp = []
                temp.append(quote_column[0])
                temp.append(quote_column[1])
                temp.append(quote_column[2])
                temp.append(quote_column[3])
                newlist.append(temp)
        
        for quote_column in distinc_in_list:
            isFound_historical = 0
            key_distinc = quote_column[0] + ":" + quote_column[1]
            n = 0
            for news_column in newlist:
                key_historical = news_column[0] + ":" + news_column[1]
                if key_historical == key_distinc or key_distinc == "Date:Symbol":
                    break
                if key_historical < key_distinc and key_distinc != "Date:Symbol":
                    temp = []
                    temp.append(quote_column[0])
                    temp.append(quote_column[1])
                    temp.append(" ")
                    temp.append(" ")
                    temp.append(quote_column[2])
                    temp.append(quote_column[3])
                    newlist.insert(n,temp)
                    break
                else:
                    n = n+1
        outcsv.writerows(newlist)
    print ('Completed.')

if __name__=="__main__":
    main()
