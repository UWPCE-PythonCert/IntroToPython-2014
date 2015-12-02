y = 4
def fun(x=y):
    print ("x is:", x)

fun()

def f(*args, **kwargs):
    print("the positional arguments are:", args)
    print("the keyword arguments are:", kwargs)

f(3,4,57,6, o=6, r=5)

print ("My name is {first} {last}".format(last="Barker", first="Chris"))

d = {"last":"Barker", "first":"Chris"}
print("My name is {first} {last}".format(**d))

def f(fore_color='w',back_color='x',link_color='y',visited_color='z'):
    print (('{},{} -- {},{}').format(fore_color,back_color,link_color,visited_color))

other = ('white', 'orange')
other2 = {'link_color':'pink', 'visited_color':'jump'}
print (other2['visited_color'])

f(other2['visited_color'], *other,visited_color='yellow')

def fun(x, a=None):
    if a is None:
        a = []
    a.append(x)
    print(a)

fun(4)
fun(10)

l = [lambda x, y: x+y]
print (l[0](2,3))