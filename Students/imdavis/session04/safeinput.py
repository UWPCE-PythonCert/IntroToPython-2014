#!/usr/bin/env python2.7

# This function takes the ^D or ^C to mean that the user wants to 
# exit the script when the script is waiting for raw_input
def safeinput(astring):
    try:
        todo = raw_input(astring + " > ")
    except (EOFError, KeyboardInterrupt):
        todo = "exit"
    return todo


# This will either print something to the screen or exit gracefully 
# when aske to exit either from the prompt or using ^C or ^D
request = None
action1 = "print"
action2 = "exit"
promptstring = "'(P)rint' or '(E)xit' ?"
promptstring2 = "Give me something to echo: "
while (request != action2):
    orig_request = safeinput(promptstring)
    request = orig_request.lower()
    if(request == "exit" or request == "e"):
        print "Ok, exiting!"
        request = "exit"
    elif(request == "print" or request == "p"):
        toprint = safeinput(promptstring2)
        if(toprint.lower() == "exit" or toprint.lower() == "e"):
            print "Ok, exiting!"
            request = "exit"
        else:
            print toprint
    else:
        print "Your request was not valid"