def fizz_buzz():
    for i in range(1,101):
        fizz_buzz = ''
        if i % 3 == 0:
            fizz_buzz += 'Fizz'
        if i % 5 == 0:
            fizz_buzz += 'Buzz'
        print(fizz_buzz if fizz_buzz else i)
        # if fizz_buzz:
        #     print(fizz_buzz)
        # else:
        #     print(i)
