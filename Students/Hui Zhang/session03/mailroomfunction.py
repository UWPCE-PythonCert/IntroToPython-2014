

def sendletter(Userlist, input1):
    # Print out all existing donators name.
    print Userlist[::2]
    username1 = raw_input("Please type a name from above existing Donator List or enter a new name: ")
    # Verify if input are all digis.
    amount1 = raw_input("Please input the amount of your donation: ")
    # Determine if your input is digi.
    while not amount1.isdigit():
        print "Error, your input is not a number!!!"
        amount1 = raw_input("Please input the amount of your donation: ")
    # Determine if the donator name just typed in is actually in the list.
    # If it is in the list, then do the below:
    if username1 in Userlist:
        locationuser1 = Userlist.index(username1)
        Userlist[locationuser1 + 1].append(int(amount1))
    # If it is not in the list, then append it in the list.
    else:
        Userlist.append(username1)
        Userlist.append([int(amount1)])
    print '\n'
    print "Thank you, " + username1 + ", for your generous donation of amount of: $" + amount1 + " Dollars ! \n\n"
    return

    if __name__ == "__main__":
        # execute only if run as a script
        main()

def printout(Userlist, input1):
    #initilize a list named donator_tuples
    donator_tuples = []
    # create a list wiht donator name, sum of donation, times of donation and average donation.
    for username2 in Userlist[::2]:
        locationuser2 = Userlist.index(username2)
        amount2 = sum(Userlist[locationuser2 + 1])
        # calculate how many times of donation
        length2 = len(Userlist[locationuser2 + 1])
        # calculate average donation
        average2 = int(amount2 / length2)
        donator_tuples.append([username2, amount2, length2, average2])
    # sort the list: donator_tuples by sum of donation.
    donator_tuples_sorted = sorted(donator_tuples, key=lambda donator: donator[1])
    print '\n\n'
    # Left align strings to be printed out
    print '{0:<10} {1:<8} {2:<8} {3:<8}'.format("Donator", "Total", "Times", "Average")
    for username3 in donator_tuples_sorted:
        # Left align strings/numbers in the sorted list: donator_tuples_sorted to be printed out
        print '{0:<10s} ${1:<7d} {2:<8d} ${3:<8d}'.format(username3[0], username3[1], username3[2], username3[3])
        print '\n'
    return

    if __name__ == "__main__":
        # execute only if run as a script
        main()
