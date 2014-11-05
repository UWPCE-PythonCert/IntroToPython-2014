
'''
The raw_input() function can generate two exceptions: EOFError or KeyboardInterrupt on end-of-file(EOF) or canceled input.
Create a wrapper function, perhaps safe_input() that returns None rather rather than raising these exceptions, when 
the user enters ^C for Keyboard Interrupt, or ^D (^Z on Windows) for End Of File.
Update your mailroom program to use exceptions (and IBAFP) to handle malformed numeric input
'''

def safe_input(prompt):
    try:
        input = raw_input(prompt)
    except EOFError:
        print "That won't work!"
        return None
    except KeyboardInterrupt:
        print "HAHAHAHA... you're stuck forever"
        return None
    return input
    
    
if __name__ == "__main__":
    trapped = True
    while trapped:
        trapString = safe_input("Try to get out: ")
        if trapString is not None:
            print "You wrote:", trapString
            if trapString.upper() == 'Q':
                trapped = False
        else:
            print "Would you like to play a game?"
            