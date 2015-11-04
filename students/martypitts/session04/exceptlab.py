def safe_input():
    try:
        UserIn = input("Provide an input:")
        return UserIn
    except EOFError:
        return "None"
    except KeyboardInterrupt:
        return "None"
    else:
        return "None"

ReadKeyboard = safe_input()
print("Value read is =", ReadKeyboard)

