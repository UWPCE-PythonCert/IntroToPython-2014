#!/usr/bin/python3
for num in range(1,101,1):
    if num%3 == 0 and num%5 == 0: #number divisible by 3 and 5 
        num = 'FizzBizz'          #replace number with FizzBizz
    elif num%3 == 0:              #numbers divisible by 3 but not by 5 
        num = 'Fizz'              #replace number with Fizz
    elif num%5 == 0:              #numbers divisible by 5 but not by 3
        num = 'Bizz'              #replace number with Bizz
    print(num)