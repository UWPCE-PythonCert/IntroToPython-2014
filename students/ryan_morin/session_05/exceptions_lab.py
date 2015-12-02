def safe_input():
    try:
        wrd = input('input information')
        return wrd
    except (EOFError, KeyboardInterrupt):
        print ('Sorry you have an error!')