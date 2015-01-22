def fun(x, y):
    pattern1 = ("+" + "-"*4)*y + "+"
    pattern2 = ("|" + " "*4)*y + "|"
    for i in range(x):
        if i % 5 == 0:
            print pattern1
        else:
            print pattern2



def FizzBuzzFrodoBilboGandalf(n):
    for i in range(n):
        x = ""
        if i % 3 == 0:
            x+="Fizz"
        if i % 5 == 0:
            x+="Buzz"
        if i % 7 == 0:
            x+="Frodo"
        if i % 11 == 0:
            x+="Bilbo"
        if i % 13 == 0:
            x+="Gandalf"
        if len(x) > 0:
            print x
        else:
            print i




# Write a function FizzBuzzFrodoBilboGandalf(n) which prints out the numbers 
# from 1 to n, replacing numbers divisible by 3 with "Fizz", numbers divisible by 5 with 
# "Buzz", numbers divisible by 7 with "Frodo", numbers divisible by 11 with "Bilbo", and 
# numbers divisible by 13 with "Gandalf".  Numbers divisible by multiple factors should display 
# "FizzBuzz", "BuzzBilboGandalf", etc.