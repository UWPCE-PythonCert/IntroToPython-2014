# fibonacci.py


def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    elif x == 0:
        return 0
    else:
        return fibonacci(x-1) + fibonacci(x-2)

for i in range(11):
    print(fibonacci(i))
