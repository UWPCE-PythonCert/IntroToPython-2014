"""
Monthly stock data selected and saved as a csv file from Yahoo Finance online.
Open csv file and present user with a menu:
Monthly open and close prices in side by side columns from Oct 1994 - Oct 2014.
Calculate monthly high avg from Oct 1994 - Oct 2014.
Calculate monthly low avg from Oct 1994 - Oct 2014.
Present user with option to quit program.
Prevent user from entering menu option other than what is presented.
'"""

import csv
import sys    # import sys is used so I can leverage an alternative to the print statement for opencloseresults( )


def menu_selection( ):
    """ presents and takes a user input to determine which function to run
    """
    uentry = raw_input( '''\nPlease Select a Number From the Data Menu Below:
        1 - The monthly open and close prices for the last 20 years
        2 - The avg monthly high for the last 20 years
        3 - The avg monthly low for the last 20 years
        4 - (Select this option when you are finished)
        ''' )
    return uentry


def highlowresults(a, b):   # function with header and row as arguments
    """ takes the High or Low column data for each month for the past 20 years and calcuates the average price.
    """
    fin = open( 'disneystock.csv', 'U' )
    finrow = csv.reader(fin)
    finrow.next( )    # skip over the initial header row
    datacolumn = [ ]    # start with empty list
    for row in finrow:
        datacolumn.append( float(row[b]) )    # convert the string for a given data column to float and create the list
    return "The avg monthly %s from Oct 1994 - Oct 2014 was %.2f" % (a, sum(datacolumn) / len(datacolumn)) # add column and divide by the length
    
    fin.close( )


def opencloseresults( out = sys.stdout ):   # optional argument included for testing purposes
    """opens the csv file, iterates through each row, formats and prints out the Date, Open and Close results
    for the past 20 years.
    """
    fin1 = open('disneystock.csv', 'U')
    finrow1 = csv.reader(fin1)    # converts each row to  list
    print "Here are the monthly open and close prices for the last 20 years:"
    finrow1.next( )    # skip over the iniitial header row
    for row1 in finrow1:
        out.write( '%10s %s %.2f %s %.2f' % ((row1[0]), '     ', float(row1[1]), '     ', float(row1[4])) + '\n' )   #  format with 2 decimal places.

    fin1.close( )


def highavg( ):
    """ contains the 'High' column index and format parameters
    """
    avghigh = highlowresults( 'High', 2 )    # assign the return results
    print avghigh    # this is a more flexible alternative to having the print statement at the end of the highlowresults function. 


def lowavg( ):
    """ contains the 'Low' column index and format parameters
    """
    avglow = highlowresults( 'Low', 3 )
    print avglow


if __name__ == "__main__":    # If the module is being run, use the following. If the module is imported (such as for testing) than don't.
    running = True
    while running:
        uentry = menu_selection( )
        if uentry == "1":
            opencloseresults( )
        elif uentry == "2":
            highavg( )
        elif uentry == "3":
            lowavg( )
        elif uentry == "4":
            print "Thank you. Come back again."
            running = False
        else:
            print "Please try again and enter a selection from the menu options."


