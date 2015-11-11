def safe_input():
    try:
        return (input("ENTER STUFF: "))
    except (EOFError, KeyboardInterrupt):
        return None

print(safe_input())