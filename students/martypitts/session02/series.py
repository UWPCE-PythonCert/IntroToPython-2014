nth = 4
fib = ["0","1","2","3","4","5","6","7","8","9","10"]
# Fibonacci Series
def fibonacci(nth):
   """ return the fibonacci series by summing the 2 previous numbers to get the next. """
   fib[0] = 0
   fib[1] = 1
   for n in range(2, 10):
      fib[n] = fib[n-2] + fib[n-1]
   return fib[nth]
# End if  


nth = input("Which number in the fibonacci series would you like?")
n = fibonacci(int(nth))
print("The nth fibonacci series value is = ", n)
