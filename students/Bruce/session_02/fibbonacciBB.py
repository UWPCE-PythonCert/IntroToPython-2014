def fib(n):
    if n<= 3: return 1
    else: return fib(n-2)+fib(n-1)
n=int(input("Enter integer greater than 1: \n"))
fibnumber = fib(n)
print("The Fibbonacci number at position ",n,"is ",fibnumber)