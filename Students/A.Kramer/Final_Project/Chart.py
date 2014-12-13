'''
Created on Dec 3, 2014

@author: Aleksey Kramer
'''
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.finance import candlestick 
import pylab

# adjusted font size for the plots
matplotlib.rcParams.update({"font.size": 10})


# define RSI function
def rsiFunc(prices, n=14):
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed >= 0].sum() / n
    down = -seed[seed<0].sum() / n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1. + rs)
    for i in range(n, len(prices)):
        delta = deltas[i-1]
        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta
        up = (up * (n-1) +upval) / n
        down = (down*(n-1) + downval) / n
        rs = up/down
        rsi[i] = 100. - 100. / (1. + rs)
    return rsi
        
# define moving average function
def movingaverage(values, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values, weights, 'valid')
    return smas # numpy array

def graphData(stock, MA1=12, MA2=26):
    try:
        # define the data file
        stockFile = "./data/" + stock + ".txt"
        
        # Load data into numpy arrays
        date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile, delimiter=",", 
                                            unpack=True, converters = {0: mdates.strpdate2num("%Y%m%d")})
        
        #-----------------------------------------------------------------------------------------------
        # building data for drawing plotting candlestick chart.  Basically, a an array of comma separated
        # values.  The order of elements is very specific, so check the documentation for candlestick
        x = 0
        y = len(date)
        candleArray = []
        while x < y:
            # order of elements matters!!! - used for candlestick charting
            appendLine = date[x], openp[x], closep[x], highp[x], lowp[x], volume[x]
            candleArray.append(appendLine)
            x += 1
        
        # moving averages for 12 and 26 days
        Av1 = movingaverage(closep, MA1)
        Av2 = movingaverage(closep, MA2)
        # Starting point for graphs
        SP = len(date[MA2-1:])
        # Creating Moving Average labels
        label1=str(MA1) + " SMA"
        label2=str(MA2) + " SMA"
        
        
        # changing the face color of the graphics       
        fig = plt.figure(facecolor="#07000D")
        
        # create room and plot candlestick chart
        ax1 = plt.subplot2grid((5,4), (1,0), rowspan=4, colspan=4, axisbg="#07000D")
        candlestick(ax1, candleArray[-SP:], width=0.75, colorup="#9EFF15", colordown="#FF1717")
        # plot moving averages
        ax1.plot(date[-SP:], Av1[-SP:], "#5998FF", label=label1, linewidth=1.5)
        ax1.plot(date[-SP:], Av2[-SP:], "#E1EDF9", label=label2, linewidth=1.5)
        # Set grid color to white
        ax1.grid(True, color="white")
        # Set number of tickers on x-axis
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        # Format date for presentation
        ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        # Change label and border colors
        ax1.yaxis.label.set_color("white")
        ax1.spines["bottom"].set_color("#5998FF")
        ax1.spines["top"].set_color("#5998FF")
        ax1.spines["left"].set_color("#5998FF")
        ax1.spines["right"].set_color("#5998FF")
        # Change tick color to white
        ax1.tick_params(axis="y", colors="white")
        ax1.tick_params(axis="x", colors="white")
        plt.ylabel("Stock Price and Volume")
        # display legend and set size of font to 7
        maLeg = plt.legend(loc=9, ncol=2, prop={"size":7}, fancybox=True)
        # update label transparency
        maLeg.get_frame().set_alpha(0.4)
        textEd = pylab.gca().get_legend().get_texts()
        # set label color
        pylab.setp(textEd[0:5], color = "white")
        # Tilt the labels to 45 degrees
        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45) 
        
        
        # set up RSI area
        ax0 = plt.subplot2grid((5,4), (0,0), sharex=ax1, rowspan=1, colspan=4, axisbg="#07000d")
        #plot RSI
        rsi = rsiFunc(closep)
        rsiCol = "#00FFE8"
        ax0.plot(date[-SP:],rsi[-SP:], rsiCol, linewidth=1.5)
        ax0.axhline(70, color = rsiCol)
        ax0.axhline(30, color = rsiCol)
        # color the spaces between the horizontal lines and the RSI line
        ax0.fill_between(date[-SP:],rsi[-SP:], 70, where=(rsi[-SP:] >= 70), facecolor=rsiCol, edgecolor=rsiCol)
        ax0.fill_between(date[-SP:],rsi[-SP:], 30, where=(rsi[-SP:] <= 30), facecolor=rsiCol, edgecolor=rsiCol)
        # Change label and border colors
        ax0.spines["bottom"].set_color("#5998FF")
        ax0.spines["top"].set_color("#5998FF")
        ax0.spines["left"].set_color("#5998FF")
        ax0.spines["right"].set_color("#5998FF")
        # Change tick color to white
        ax0.tick_params(axis="x", colors="white")
        ax0.tick_params(axis="y", colors="white")
        ax0.set_yticks([30,70])
        ax0.yaxis.label.set_color("white")
        plt.ylabel("RSI")
        
        
        # Plot volume on the same range as ax1
        volumeMin = 0 
        ax1v = ax1.twinx()
        # subtract moving average calculations
        ax1v.fill_between(date[-SP:], volumeMin, volume[-SP:], facecolor="#00FFE8", alpha=.5)
        ax1v.axes.yaxis.set_ticklabels([])
        # hide grid
        ax1v.grid(False)
        # Change label and border colors
        ax1v.spines["bottom"].set_color("#5998FF")
        ax1v.spines["top"].set_color("#5998FF")
        ax1v.spines["left"].set_color("#5998FF")
        ax1v.spines["right"].set_color("#5998FF")
        # update the height of the volume part
        ax1v.set_ylim(0,3*volume.max())
        # Change axis color
        ax1v.tick_params(axis="x", colors="white")
        ax1v.tick_params(axis="y", colors="white")
        
        
        # Setting up the overall appearance of the plot
        plt.subplots_adjust(left=.08, bottom=.14, right=.95, top=.95, wspace=.20, hspace=0)
        plt.suptitle(stock, color="white")
        plt.setp(ax0.get_xticklabels(), visible=False)
        plt.show()
        fig.savefig("./data/" + stock + ".png", facecolor=fig.get_facecolor())
        
    except Exception, e:
        print "main loop", str(e)
        
if __name__ == "__main__":
    # testing the calls
    # a list of stocks to process (for testing)
    stocksToPull = 'AAPL', 'GOOG', 'AMZN', 'EBAY', 'CMG', 'MSFT', 'C', 'BA', 'TSLA'
    
    graphData(stocksToPull[3])
    

