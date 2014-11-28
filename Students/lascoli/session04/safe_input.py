"""Creating Wrapper Function Safe Input """
def safe_input(msg):
"""Function is called when ^C or ^D occurs"""
try:
    x = raw_input(user_action)
except (EOFError, KeyboardInterrupt):
    return None
else:
    return variaxble
if __name__ == "__main__":