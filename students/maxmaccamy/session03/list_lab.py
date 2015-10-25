__author__ = 'Max MacCamy'

def main():
    """
    When ran this function acomplishes the following:
    - Creates a list that contains "Apples", "Pears",
    "Oranges" and "Peaches"
    - Displays the list.
    - Asks the user for another fruit and adds it to
    the end of the list.
    - Displays the list.
    - Asks the user for a number and display the number
    back to the user and the fruit corresponding to that
    number (on a 1-is-first basis).
    - Add another fruit to the beginning of the list using
    "+" and display the list.
    - Add another fruit to the beginning of the list using
    insert() and display the list.
    - Display all the fruits that begin with "P", using a
    for loop.
    :return: None
    """
    seq = ["Apples", "Pears", "Oranges", "Peaches"]
    print(seq)
    userInput = input("Type a fruit to be added to the end of the list:\n")
    seq.append(userInput)
    print(seq)

    # Continually query the user for a 1-based index into the sequence of fruits
    while(True):
        seqLen = len(seq)
        userInput = input("Type an integer between 1 and {}:\n".format(seqLen))

        if validInteger(userInput):
            # A valid integer has been received.
            # Convert index from 1-based index to 0-based index.
            i = int(userInput) - 1
            if (i >= 0) and (i < seqLen):
                # A valid user index has been received
                print("{index}: {fruit}".format(index = i + 1, fruit = seq[i]))
                userInput = input("Type a fruit to be added to the beginning of the list:\n")

                # Add the user fruit to the beginning of the list using the "+" overload.
                seq = [userInput] + seq
                print(seq)
                userInput = input("Type another fruit to be added to the beginning of the list:\n")

                # Add the user fruit to the beginning of the list using the insert() function.
                seq.insert(0, userInput)
                print(seq)

                print("Here are all the fruits starting with 'P':")

                # Iterate over the list using a for loop and print out all elements that begin with 'P'.
                for fruits in seq:
                    if fruits.upper().startswith('P'):
                        print(fruits)
                break
            else:
                # Warn the user that their given index is out of bounds.
                print("Input is out of bounds!")
        else:
            # Warn the user that their given index is not an integer.
            print("That's not an integer!")

    return None

def validInteger(input):
    """
    Checks if the input can be converted to an integer.
    :param input:
    :return: True if input can be converted to an integer,
             otherwise False
    """
    try:
        val = int(input)
        return True
    except ValueError:
        return False

# Execute main()
main()







