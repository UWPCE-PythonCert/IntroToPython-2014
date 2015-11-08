safeStr = ""
def safe_input (name):
    try:
        safeStr = input("please provide your first name:")
        return"Hi {0}, I hope you are having a great day!".format(safeStr)
    except (KeyboardInterrupt, EOFError):
        return None
    return safe_input

print (safe_input(safeStr))
