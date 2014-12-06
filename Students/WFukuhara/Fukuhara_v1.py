"""
Monthly stock data selected and saved as a csv file from Yahoo Finance online.
Open csv file and present user with a menu:
Monthly open and close prices in side by side columns from Oct 1994 - Oct 2014.
Calculate monthly high avg from Oct 1994 - Oct 2014.
Calculate monthly low avg from Oct 1994 - Oct 2014.
Present user with option to quit program.
Prevent user from entering menu option other than what is presented.
'"""

# keep the reading of the file separate. Open and put in memory. Then the access that funtion so you don't need to open/read within each function
# use class structure. Then access the attributes and methods of the class.


import csv


def menu_selection( ):
    uentry = raw_input('''\nPlease Select a Number From the Data Menu Below:
        1 - The monthly open and close prices for the last 20 years
        2 - The avg monthly high for the last 20 years
        3 - The avg monthly low for the last 20 years
        4 - (Select this option when you are finished)
        ''' )
    return uentry


def highlowresults(a, b):   # function with header and row as arguments
    fin = open('disneystock.csv', 'U')
    finrow = csv.reader(fin)
    finrow.next( )    # skip over the initial header row
    datacolumn = [ ]    # start with empty list
    for row in finrow:
        datacolumn.append(float(row[b]))    # convert the string for a given data column to float and create the list
    print "The avg monthly %s from Oct 1994 - Oct 2014 was %.2f" % (a, sum(datacolumn) / len(datacolumn)) # add column and divide by the len
    
    fin.close( )


def opencloseresults( ):
    fin1 = open('disneystock.csv', 'U')
    finrow1 = csv.reader(fin1)
    print "Here are the monthly open and close prices for the last 20 years:"
    finrow1.next( )    # skip over the iniitial header row
    for row1 in finrow1:
        print '%10s %s %.2f %s %.2f' % ((row1[0]), '     ', float(row1[1]), '     ', float(row1[4]))    #  format with 2 decimal places

    fin1.close( )


def highavg( ):
    highlowresults('High', 2)


def lowavg( ):
    highlowresults('Low', 3)


if __name__ == "__main__":    # If the module is being run, use the following. If the module is imported than don't.
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


