'''
Class to create GUI interface for users to select visualiztion options
'''

import tkinter
from Functions import Create_Chart, Create_Table, Import_CSV

# Create GUI with buttons to generate a chart, table, or both
class GUI(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_user_interface()
        self.symbol = []
        self.age = []
        Import_CSV() # imports CSV lists

    # Define funtion for 'Chart' button.
    def Chart(self):
        print("Generating Chart, this could take a second")
        Create_Chart()
        print("Chart Finished")
    
    # Define function for 'Table' Button
    def Table(self):
        print("Generating Table, this could take a second")
        Create_Table()
        print("Table Finished, Look under main folder for TXT file")
       
    # Define function for 'Both' button     
    def Both(self):
        print("Generating Table then Chart, this could take a second")
        Create_Table()
        print("Finished Table, Look under main folder for TXT file")
        print("Generating Chart")
        Create_Chart()
        print("Finished Both, Look under main folder for TXT file")

    # funtion to load GUI
    def initialize_user_interface(self):
        # format GUI pop-up
        self.parent.title("Stock Ownership Summary") # title
        self.parent.grid_rowconfigure(0, weight = 6) 
        self.parent.grid_columnconfigure(0, weight = 6)
        
        # instructions for users
        tkinter.Label(text="Save the 'Stocks.csv' file in 'Data' Folder", 
                      fg="white", bg="black").grid(row = 0, column = 0, sticky = tkinter.E)
        tkinter.Label(text="Select 'Chart' to generate a chart showing the price change over your ownership life",
                      fg="black").grid(row = 2, column = 0, sticky = tkinter.E)
        tkinter.Label(text="Select 'Table' to gerentate a summary of the value change since you purchased stocks", 
                      fg="black").grid(row = 4, column = 0, sticky = tkinter.E)
        tkinter.Label(text="Table will be saves as 'Summary.txt'", 
                      fg="black").grid(row = 5, column = 0, sticky = tkinter.E)
        tkinter.Label(text="Select 'Both' to generate both at Table and a Chart", 
                      fg="black").grid(row = 7, column = 0, sticky = tkinter.E)
        tkinter.Label(text="", 
                      fg="black").grid(row = 1, column = 0, sticky = tkinter.E)
        tkinter.Label(text="", 
                      fg="black").grid(row = 3, column = 0, sticky = tkinter.E)
        tkinter.Label(text="", 
                      fg="black").grid(row = 6, column = 0, sticky = tkinter.E)        

        #create buttons
        tkinter.Button(self.parent,
                       text = "Chart",
                       command = self.Chart
                       ).grid(row = 2, column = 1, sticky = tkinter.E)
        tkinter.Button(self.parent,
                       text = "Table",
                       command = self.Table
                       ).grid(row = 5, column = 1, sticky = tkinter.E)
        tkinter.Button(self.parent,
                        text = "Both",
                        command = self.Both
                        ).grid(row = 7, column = 1, sticky = tkinter.E)
    
