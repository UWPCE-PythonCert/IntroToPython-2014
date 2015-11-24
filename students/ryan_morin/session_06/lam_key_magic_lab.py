l = []
def function_builder(num):
    for i in range(num):
        l.append(lambda num, e=i: num+e)
    return l

the_list = function_builder(4)
print (the_list[1](2))

for f in the_list:
    print(f(5))