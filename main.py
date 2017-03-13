"""
' This is the main program to invoke all the process
'
"""

import sys
import csv
import os 
from itertools import groupby


in_file = 'config/config.txt'

def main():
    with open(in_file, 'r') as inf:
        input  = inf.read()
        list = input.split(',')
        for x in list:
            print (x)
            os.system('python parseNews.py ' + x)
            os.system('python selectDup.py ' + x)
            os.system('python parseQuote.py ' + x)
            os.system('python consolDataEach.py ' + x)
        os.system('python consolDataAll.py')
if __name__=="__main__":
    main()
