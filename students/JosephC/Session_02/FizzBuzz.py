#Intro to Python (via the University of Washington)

#Fizzbuzz is said to be a problem many interviewees cannot adequately answer
#Odd, isn't it?

#Completed by: Joseph Cardenas, 10.17.2015



def fizzbuzz():
    n = 0 
       
    while n != 100:
        n += 1
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")

        elif n % 3 == 0:
            print("Fizz")
            
        elif n % 5 == 0:
            print("Buzz")

        
        
        else: print(n)
        

fizzbuzz()
