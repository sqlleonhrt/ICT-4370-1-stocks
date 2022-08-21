'''
Single location for commonly used / editted variable
'''

import sys

# investements CSV file location
csv_file = "Data\Stocks.csv"

# location to save table calculations
output_file = "Summary.txt"

# convert file location to class readable format
csv_file_all = [csv_file]

# variables from CSV
symbol_all = []
pur_date_all = []
no_shares = []
pur_price = []

# variable for printing to file
original_stdout = sys.stdout


