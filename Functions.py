'''
Functions to run multiple classes
'''

from matplotlib import pyplot as plt
from Variables import csv_file_all, output_file, original_stdout, symbol_all, pur_date_all, no_shares, pur_price
from Class_Chart import Chart
from Class_Table import Table
from Class_CSV import CSV
import sys

# runs Chart class to populate chart data and then generate chart
def Create_Chart():
    # populate chart data
    for (symbol, pur_date) in zip(symbol_all, pur_date_all):
        df = Chart(symbol, pur_date)
        df.Generate_Chart()

    # generate chart
    plt.title('Share Price Over Time')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend(loc='best')
    plt.gcf().autofmt_xdate(rotation=25)
    plt.show()
    
# runs Table class to create TXT file with portfolio value summaries
def Create_Table():
    # creates text file and writes any 'print' statements to the file
    with open(output_file, 'w') as f:
        sys.stdout = f
        
        # run 1 instance of Header function for formating
        df = Table(1, 1, 1)
        df.Header()
        
        # loop through portfolio data to populate body of table / TXT file
        for (symbol, shares, cost) in zip(symbol_all, no_shares, pur_price):
            df = Table(symbol, shares, cost)
            df.Main()
        sys.stdout = original_stdout
        
# load CVS data into lists
def Import_CSV():
    for csv in csv_file_all:
        df = CSV(csv)
        df.Import_CSV()

