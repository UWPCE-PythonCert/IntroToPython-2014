Fred_Flintstone = [1000, 500, 700]
Wilma_Flintstone = [500]
Barney_Rubble = [50]
Betty_Rubble = [2000, 1000]
Cary_Granite = [2500, 3000, 5000]
d = {'name':'Chris', 'city':'Seattle', 'cake':'chocolate'}
donor_list_dict = {'Fred_Flintstone':'int(len(Fred_Flintstone)),int(Fred_Flintstone)','Wilma_Flintstone':'len(Wilma_Flintstone),\
Wilma_Flintstone','Barney_Rubble':'len(Barney_Rubble),Barney_Rubble','Betty_Rubble':'len(Betty_Rubble),\
Betty_Rubble','Cary_Granite':'len(Cary_Granite),Cary_Granite'}
print('is dict properly constructed?',donor_list_dict)
#if (donor_list_dict['Betty_Rubble']):
#    print ('Huraay!')
# ann magrock, perry masonry,

def Greeting():
    print("Greetings",'\n',"Would you like to send a thank you or create a report?",'\n')
    print("Enter 1 to create a report or 2 to generate a thank you",'\n')
    response = int(input())
    print('value = ', response)
 #   type(response)
    if response == 1:
        return response
    elif response == 2:
        return response
    else:
        print ("invalid input.  exiting program")
        response = 0
        return response

#def donor_status(donor_name_concat, donor_list):
def donor_status(donor_name_concat, donor_list_dict):
    """
    This module receives two inputs (donor_name_concat, donor_list_dict).
    The module determines whether donor_name_concat is in donor_list_dict.
    If donor_list contains donor_name_concat then the module returns
    a string called donor_information containing four outputs
    ("True", donor_name_concat, number of donations, total value of donation).
    If donor_list does not contain donor_name_concat then the module returns
    a string called donor_status_data containing one output of "False".
    """
    #print('printed from donor status\n', donor_name_concat, '\n',donor_list_dict, '\n')                              #diagnostic
    #print(donor_list_dict[donor_name_concat])
    #if (donor_name_concat) in donor_list:
    if (donor_list_dict[donor_name_concat]):
        print ('Headed through if statement')
        #donor_index = donor_list_dict.index(donor_name_concat)
        donor_donation_string = donor_list_dict[donor_name_concat]
        print('\n\nmy donation string value = ', donor_donation_string[1], '\n\n')
        donor_donation = sum(donor_donation_string[1])
        print ('my summed value = ', donor_donation)
        #donor_donation_string = sum(donor_list_dict[donor_name_concat][1])
        #donor_information = ('True', donor_list[donor_index], donor_list[donor_index + 1], donor_donation)
        donor_information = (True, 'Nancy Reagan', int(3), int(2500))
        return donor_information
    else:
        print('nada')
        donor_information = ('False')
        return donor_information


def acquire_donor_name():
    print("Enter full name (first and last) of donor")
    donor_name = str(input())
    split_donor_name = donor_name.split()
    donor_firstName, donorlastName = split_donor_name[0],split_donor_name[1]
    s = "_";
    seq = (donor_firstName, donorlastName); # Make a list of donor name.
    donor_name_concat = s.join( seq)
    print('Returning ', donor_name_concat, ' and exiting acquire_donor_name\n')
    return donor_name_concat

#Run Program
#################
response = int(Greeting())
print ('response to greeting - ', response)
if response == 1 :  #create a report
    print ('running if')
    donor_name_concat = acquire_donor_name()
    print(donor_name_concat)
    donor_information = donor_status(donor_name_concat, donor_list_dict)
    print ('Now for donor information - ', donor_information)
elif response == 2 :  #write a thank you note
    print ('running if for selection 2\nRunning acquire_donor_name\n')
    donor_name_concat = acquire_donor_name()
    print('back in main program reprinting ',donor_name_concat, 'calling donor_status\n')
    donor_information = donor_status(donor_name_concat, donor_list_dict)
    print (donor_information)
    print ('\nDear', donor_name_concat,',\n')
    print ('Thank you for your', donor_information[2], 'donations totalling $', donor_information[3],'\n')
    print ('Sincerely,\nMr.Slate')



#    donor_information = donor_status(donor_name_concat, donor_list)

#donor_name_concat = ('Wilma_Flintstonea')

#print ('the donor information: ', donor_information)
