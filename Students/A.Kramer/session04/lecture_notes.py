'''
Created on Oct 21, 2014

@author: Aleksey
'''

def inClass():
      
    l = range(10)
    
    for i in range(len(l)):
        print i
    print
    
    # iterate over the tuples in the list
    l = [(1,2), (3,4), (5,6)]
    
    for i, j in l:
        print i, j
    print
    
    # zip function
    l1 = [1,2,3]
    l2 = [4,5,6]
    print zip(l1, l2)
    for i, j in zip(l1, l2):
        print i, j
    print
    
    # returns tuple
    k = ["Aleksey", "is", "my", "name"]
    for i in enumerate(k):
        print i

    # sorting example
    fruits = ["Apple", "Pears", "Oranges", "Peaches"]
    numbers = range(4)
    combined = zip(fruits, numbers)
    combined.sort()
    print combined
    
    # sorting by a key
    # need to create a function to pass to sort via key argument
    # the example is below
    def MySort(item):
        return item[1]
    
    fruits = ["Apple", "Pears", "Oranges", "Peaches"]
    numbers = range(4)
    combined = zip(fruits, numbers)
    combined.sort(key=MySort)
    print combined

    def print_me(nums):
        s = str(nums).strip("()")
        print "Print the first %d numbers: %s"%(len(nums),s)
    print_me((2,3,4,5))
    
    d = {}
    d["Aleksey"] = "Kramer"
    d["Jon"] = "Doe"
    d["Jane"] = "Doe"
        
    print d
    print d.__contains__("Aleksey")
    print d.keys()
    print d.values()
    
    d["My"] = "Name"
    
    print "%s, %s"%(d.keys(), d.values())
    
    print "Aleksey" in d
    print "Nona" in d
    print d.items()
    
    for i, j in d.items():
        print i, j
        
    d = {}
    d["name"] = "Chris"
    d["city"] = "Seattle"
    d["cake"] = "Chocolate"
    
    print d
    d.__delitem__("name")
    d.pop("city")
    print d
    d["fruit"] = "Mango"
    print d
    print "cake" in d
    print "fruit" in d
    
    
    
if __name__ == "__main__":
    inClass()