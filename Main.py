"""
    Author : Joe Moorehead
    Date : 8/20/2022
    Purpose : Visualize and summarize stock values of portfolio
    
    Required installs:
        pip install yfinance
        pip install tkinter
        pip install pandas
        pip install matplotlib
    
    Notes:
        save portfolio data as "Stocks.csv" under the "Data" folder.  Use the following format:
        SYMBOL,NO_SHARES,PURCHASE_PRICE,CURRENT_VALUE,PURCHASE_DATE
        
        A GUI will pop up with button options to visualize data


"""

import tkinter
from Class_GUI import GUI

# main funtion to generate GUI
def main():
    root = tkinter.Tk()
    b = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


