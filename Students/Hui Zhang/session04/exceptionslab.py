"""
   Create a wrapper function, perhaps safe_input() that returns None rather rather than raising
   these exceptions, when the user enters ^C for Keyboard Interrupt, or ^D (^Z on Windows) for
   End Of File.
"""
def safe-input():
    try:
        test_exception = raw_input("Please type something and press Ctrl+C\n Or\n Just press Ctrl+D without typing anything\n to test exceptions: ")
        return test_exception
    except (KeyboardInterrupt, EOFError):
        print 'Exception has been succesfully caught'
        return(None)
