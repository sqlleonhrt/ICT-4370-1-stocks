'''
Class to fill and generate a chart of stock prices since purchase.
'''

import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt

# Generate Chart using data from yfinance
class Chart:
    def __init__(self, symbol, pur_date):
        self.symbol = symbol
        self.pur_date = pur_date

    # find the closing price of stock each day since purchase
    def Closing_Price(self):
        start_date = pd.to_datetime(self.pur_date) #format date data
        Asset = pd.DataFrame(yf.download(self.symbol, # pull data from yahoo
                                         start=start_date,
                                         interval='1d',
                                         progress=False,
                                         rounding=True)
                             ['Close'])
        return Asset
    
    # populate chart
    def Generate_Chart(self):
        data = self.Closing_Price() # pull closing values from yahoo
        plt.plot(data, label=self.symbol) # populate chart data in matplot

