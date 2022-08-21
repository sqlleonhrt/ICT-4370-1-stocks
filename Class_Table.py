'''
Class to pull latest close value for all portolio stocks and calculate increase in value since purchase
'''


import pandas as pd
from Class_Chart import Chart

# find last business day
ts = pd.to_datetime("today")
offset = pd.tseries.offsets.BusinessDay(n=1)
bus_day = ts - offset

# class to create stock table and export to TXT file
class Table(Chart):
    def __init__(self, symbol, shares, cost):
        self.symbol = symbol
        self.shares = shares
        self.cost = cost
        self.pur_date = bus_day #set purchase day to last business day to pull only the latest close value
        self.cur_price = ''

    # pull current stock price for each stock in portfolio
    def Latest_Close(self):
        data = self.Closing_Price()
        self.cur_price = float(data["Close"])

    # create header for table
    def Header(self):
        # Print header
        print(f'|'
              f'{"Stock":^10}|'
              f'{"Share % Change":^15}|'
              f'{"Share $ Change":^15}|'
              f'{"Total Value":^15}'
              f'|')
    
    # run calculate and generate body of table
    def Body(self):
        # calculations for table
        per_change = self.cur_price / self.cost
        value_chage = self.cur_price - self.cost
        total_value = self.shares * self.cur_price

        # Print body
        print(f'|'
              f'{self.symbol:^10}|'
              f'{per_change:^15.2f}|'
              f'{value_chage:^15.2f}|'
              f'{total_value:^15.2f}'
              f'|')

    # used in Create_Table function loop
    def Main(self):
        self.Latest_Close()
        self.Body()
