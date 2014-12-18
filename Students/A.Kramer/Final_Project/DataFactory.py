'''
Created on Nov 28, 2014

@author: Aleksey Kramer
'''
import os
import time
import urllib2
import datetime

def pullStockData(stock):
    # check if data directory exists, if not, create
    if not os.path.exists("./data"):
        os.makedirs("./data")

    # print out the pull time
    print "Pulling stock", stock, "\t",
    print str(datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))

    # define url and file
    urlToVisit = "http://chartapi.finance.yahoo.com/instrument/1.0/" + stock + "/chartdata;type=quote;range=1y/csv"
    saveFileLine = stock + ".txt"

    # Determine the time of the last entry in the file, if file exists
    # set the last Unix time to 0, if file dies not exist
    try:
        existingData = open("./data/" + saveFileLine, "r")
        allLines = existingData.read()
        splitExisting = allLines.split("\n")
        lastLine = splitExisting[-2]
        lastUnix = int(lastLine.split(",")[0])
        existingData.close()
    except Exception, e:
        print "Pulling data: Determining last date", e
        lastUnix = 0

    # Obtain data for the ticket from Yahoo finance and split the file by new line
    sourceCode = urllib2.urlopen(urlToVisit).read()
    splitSource = sourceCode.split("\n")

    # Open file for writing and filter out the data to ensure that
    # each line contains 6 entries separated by comma
    # no 'visited' in the line
    # and the timing in the entries for each record is greater than the last one already
    # stored in existing file
    saveFile = open("./data/" + saveFileLine, "a")
    for eachLine in splitSource:
        if "values" not in eachLine:
            splitLine = eachLine.split(",")
            if len(splitLine) == 6:
                # assure we are only getting new data in the file
                if int(splitLine[0]) > lastUnix:
                    lineToWrite = eachLine + "\n"
                    saveFile.write(lineToWrite)
    saveFile.close()

    # Print out logging info and make program sleep for 1 second
    print "Pulled Stock", stock
    print "Sleeping....."
    print str(datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(3)


# Pull the data for selected stocks
if __name__ == "__main__":
    # Testing data pull
    stocksToPull = 'AAPL', 'GOOG', 'AMZN', 'EBAY', 'CMG', 'MSFT', 'C', 'BA', 'TSLA'
    pullStockData(stocksToPull[3])

