__author__ = 'Max MacCamy'

def main():
    """
    Executes each step of the list lab.
    :return: None
    """
    print("Running exercise 1...")
    seq = listLabExercise1();

    print("\nRunning exercise 2...")
    listLabExercise2(seq)

    return None

def listLabExercise1():
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
    :return: List of fruits manipulated by a user.
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

    return seq

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

def listLabExercise2(seq):
    """
    Takes a list and performs the following:
    - Displays the list
    - Removes the last fruit from the list
    - Displays the list
    - Asks the user for a fruit to delete and find it and delete it.
    :param seq: Sequence to operate on
    :return: None
    """
    # Display the list
    print(seq)

    # Remove last fruit from the list
    seq.pop()

    # Display the list
    print(seq)

    while(True):
        # Ask the user for a fruit to delete and find it and delete it.
        userInput = input("Which fruit would you like to delete? (case sensitive)\n")

        # Ignore case by making all the elements of the list lowercase
        if (seq.count(userInput) > 0):
            seq = removeItemFromList(seq, userInput)
            print(seq)
            break;
        else:
            print("Fruit doesn't exist in list")

    return None

def removeItemFromList(theList, item):
    return [value for value in theList if value != item]

# Execute main()
main()







