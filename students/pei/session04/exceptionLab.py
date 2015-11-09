def safe_input (prompt):
    try:
        safeStr = input(prompt)
        return"Hi {0}, I hope you are having a great day!".format(safeStr)
    except (KeyboardInterrupt, EOFError):
        return None
    return safe_input

print (safe_input("Please enter your first name:"))
