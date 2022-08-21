import pandas as pd
from Variables import symbol_all, pur_date_all, no_shares, pur_price
import csv


class CSV:
    def __init__(self, csv):
        self.csv = csv

    def Import_CSV(self):
        try:
            x = open(self.csv)
        except FileNotFoundError:
            print(f"\n The file path is invalid,\n"
                  f"\n Please enter the correct path in Variables.py")
        file = csv.DictReader(open(self.csv, 'r'))
        for col in file:
            # correct obsolete stock symbols
            if col['SYMBOL'] == 'RDS-A':
                col['SYMBOL'] = 'SHEL'
            if col['SYMBOL'] == 'FB':
                col['SYMBOL'] = 'META'
            symbol_all.append(col['SYMBOL'])
            date = pd.to_datetime(col['PURCHASE_DATE'])
            pur_date_all.append(date)
            no_shares.append(int(col['NO_SHARES']))
            pur_price.append(float(col['PURCHASE_PRICE']))
