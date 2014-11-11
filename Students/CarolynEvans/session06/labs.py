def function_builder(num):
    l=[]
    for y in range(0, num):
        l.append(lambda x=y, y=num: x+y)

    return l

def function_builder_comprehension(num):
    l = [lambda x=y, y=num: x+y for y in range(0,num)]

    return l

print "\nfunction list built with loop"
x=4
the_list = function_builder(x)
for i in range(x):
    print "{} + {} = {}".format(i, x, the_list[i](i))

print "\nfunction list built with comprehension"
x=4
the_list = function_builder_comprehension(x)
for i in range(x):
    print "{} + {} = {}".format(i, x, the_list[i](i))








