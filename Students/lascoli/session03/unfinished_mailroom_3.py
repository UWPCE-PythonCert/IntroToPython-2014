#Create a data structure with 2 elements (Name, Dollar Amount Donated)

donor_list = ['Mick Jagger','$500.00',
'Jimmy Page','$200.00',
'Robert Plant','$100.00',
'Roger Daltry','$400.00',
'Pete Townsend','$250.00',
'Eric Clapton','$500.00',
'Mick Jagger','$700.00',
'Eric Clapton','$200.00',
'Pete Townsend','$950.00',
'Robert Plant','$800.00',
'Mick Jagger','$400.00',
'Roger Daltry','$750.00',
'Pete Townsend','$750.00',
'Eric Clapton','$900.00',
'Mick Jagger','$500.00',
'Robert Plant','$800.00',
'Roger Daltry','$600.00',]

def write_thk_letrs(user_input2):
#Write a letter thanking a donor#
    
    print ("Dear %s. \n\nThank you for your generous contribution !\n\nYou Rock !\n\n" % (user_input2))    
    return main()


def thanks_note():
    user_input2 =raw_input('Please provide the full name of the donor, or type "list for a list of donors" :\n\n')
    
    if user_input2 == 'list':
        tmp_list1= []
        tmp_list2= []
        i = ""
        tmp_list1 = donor_list[0::2]
        for i in tmp_list1:
            if i not in tmp_list2:
                tmp_list2.append(i)
        for x in tmp_list2:
            print ("\n" + x + "\n")
        return add_donor()

    else:
        for d_name in donor_list:
            if d_name == user_input2:
                return write_thk_letrs(user_input2)


def add_donor():
    user_input2 =raw_input('Please provide the full name of the donor, or type "list for a list of donors" :\n\n')
    for d_name in donor_list:
        
        if d_name != user_input2:
            break 
        
    while True:
        user_input3 = raw_input("\n" + user_input2 + " is a new donor,and can be added to the donor list.\n " " \nWould you like"
    " to make a donation for " + user_input2 + " ?\n\nPlease answer 'Yes' or 'No' ")
        
        if user_input3 == "No":
            main()

        if user_input3 == "Yes":
            break

    while True:
        user_input4 = raw_input('Enter the donation amount \n\n ')
        
        #if user_input3 == 'menu':
            #return 'menu'
        try:
            user_input4 = float(user_input4)
            break
        
        except ValueError:
            print 'Specified Donations must be a in a numeric format, renter amount.'  

    
    user_input4 = "$"+str(user_input4)
    donor_list.extend([user_input2, user_input4])
    write_thk_letrs(user_input2)

def donor_report():

    tmp_list3= []
    tmp_list4= []
    user_input5 =""
    i = ""
    tmp_list3 = donor_list[0::2]

    print("\n\nDonor Name     Total Amount Donated     Number of Donations     Average Donation\n" )
    for i in tmp_list3:
        if i not in tmp_list4:
            tmp_list4.append(i)
    for x in tmp_list4:
            print ("\n" + x + "\n")
       
def main():

    
    while True:
        user_input1 = ''
        user_input2 = ''
        user_input3 = ''
        user_input4 = ''
        user_input4 = ''
        
        user_input1 = raw_input('Welcome to the Donations Support Program\n\n'
            'Please enter a 1 to Send a Thank You Note \n\n'
            'Please enter a 2 to Create a Report \n\n'
            'Please enter a 3 to exit this project \n\n')


        if user_input1 == '1':
            #print("Send a Thank You Note")        
            return thanks_note()
            

        if user_input1 == '2':
            #print("Create a Report")
            return donor_report()
        

        if user_input1 == '3':
            print ("Exiting this Program")
            break
    
                 

if __name__ == '__main__':
    main()


