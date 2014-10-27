from mailroomfunction import sendletter
from mailroomfunction import printout

Userlist = ['Jerry', [10, 20, 30], 'Peter', [5, 6], 'Aly', [3, 4], 'Anisha', [11, 15, 13], 'Chris', [9, 11, 14], 'Vini', [13, 17, 16]]

input1 = input("To send a Thanks You letter, press '1'\nTo create a report, press '2'\nTo Exit, press '0' \n")

while input1:
    if input1 == 1:
        sendletter(Userlist, input1)
        input1 = input("To send a Thanks You letter, press '1'\nTo create a report, press '2'\nTo Exit, press '0' \n")
    elif input1 == 2:
        printout(Userlist, input1)
        input1 = input("To send a Thanks You letter, press '1'\nTo Create a report, press '2'\nTo Exit, press '0' \n")
