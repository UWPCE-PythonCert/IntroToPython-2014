'''
Created on Dec 3, 2014

    The code pulls one year worth of data for the stock of your choice
    and graphs the data using matplotlib, displaying candlestick chart,
    simple moving averages for 12 and 26 days (default), and a Relative
    Strength Index (RSI) for selected stock.
    
    I found an excellent video tutorial on financial graphing with python
    that shows how to use matplotlib, change parameters of the plots
    and to do math calculation to derive moving averages and RSI indexes.
    The tutorial can be found on this web site: http://sentdex.com/
    This is excellent source to learn charting with matplotlib

@author: Aleksey Kramer
'''
from Chart import graphData
from DataFactory import pullStockData

def runCode():
    ''' Execute code for final project '''
    answer = raw_input("Enter The stock to graph: ")
    pullStockData(answer.upper().strip())
    graphData(answer.upper().strip())
    
# run main program
if __name__ == "__main__":
    runCode()
    