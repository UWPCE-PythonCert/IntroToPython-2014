def fizz_buzz():
    for i in range(1,101):
        fizz = ''
        buzz = ''
        if i % 3 == 0:
            fizz = 'Fizz'
        if i % 5 == 0:
            buzz = 'Buzz'
        if fizz or buzz:
            print(fizz + buzz)
        else:
            print(i)