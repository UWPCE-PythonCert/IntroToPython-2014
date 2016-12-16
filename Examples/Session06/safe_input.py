def safe_input():
    try:
        the_input = input("\ntype something >>> ")
    except (KeyboardInterrupt, EOFError) as error:
        print("the error: ", error)
        error.extra_info = "extra info for testing"
        # raise
        return None
    return the_input

def main():
    safe_input()

def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError as err:
        print("you put in a zero!!!")
        print("the exeption:", err)
        err.args = (("very bad palce for a zero",))
        err.extra_stuff = "all kinds of things"
        raise

# if __name__ == '__main__':
#     main()