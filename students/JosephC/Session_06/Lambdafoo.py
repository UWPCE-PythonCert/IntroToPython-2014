#Lambdafoo
'''Write a function that returns a list of n functions, such that each one, when called, will return the input value, 
incremented by an increasing number.'''

#very similar to the sample gave in class
l = []


for i in range(3):
    l.append(lambda x, e=i: x+e)

for f in l:
    print(f(3))




















def Lambdafoo(n):
    l = []

    for i in range(n):
        l.append(lambda x, i: x+i)

    for f in l:
        print(f(n))

Lambdafoo(3)

    
	
