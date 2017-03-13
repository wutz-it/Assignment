"""
' This program is used for consolidate all quote close and volume information with
' all news and sort them by date
"""

import sys
import csv
import os, os.path
import glob
from datetime import *
from itertools import groupby

out_file = 'result/consolidated_report.csv'
directory = os.path.dirname(out_file)
if not os.path.exists(directory):
    os.makedirs(directory)
def main():
    print ('Start consolidate quotes and news altogether.')
    DIR = 'report'
    newlist = []
    with open(out_file, 'w', newline='') as outf:
        outcsv = csv.writer(outf)
        for filename in glob.glob(DIR + '/*.csv'):
            with open(filename, 'r') as input_inf:
                input_incsv  = csv.reader(input_inf)
                input_in_list = list(input_incsv)
                if len(newlist) == 0:
                    for x in input_in_list:
                        newlist.append(x)
                else:
                    for x in input_in_list: 
                        key_distinc = x[0] 
                        if key_distinc != "Date":
                            newdate1 = datetime.strptime(key_distinc, "%m/%d/%Y")
                            n =0
                            for y in newlist:
                                key_historical = y[0] 
                                if key_historical != "Date":
                                    newdate2 = datetime.strptime(key_historical, "%m/%d/%Y")
                                    if newdate2 < newdate1:
                                        newlist.insert(n,x)
                                        break
                                    else:
                                        n = n+1
                                else:
                                    n = n+1
        outcsv.writerows(newlist)
    print ('Consolidated data is completed. \nSee the result in \'result/consolidated_report.csv\' ')
if __name__=="__main__":
    main()
