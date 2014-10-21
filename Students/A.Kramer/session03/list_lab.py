
def list_lab():
    
    # Part 1
    print "Part 1\n"
    lst = ["Apples", "Pears", "Oranges", "Peaches"]
    print lst
    fruit = raw_input("Enter another fruit: ")
    lst.append(fruit)
    print lst
    num = raw_input("Enter the nubmer: ")
    print num, lst[int(num) -1]
    print lst
    lst.insert(0, "Grape")
    print lst
    for i in lst:
        if i[0] == 'P':
            print i, 
    
    # Part 2
    print "\n\nPart 2\n"
    print lst
    lst.remove("Grape")
    print lst
    frt = raw_input("Enter the fruit to delete: ")
    print lst.remove(frt)
    print lst
    
    # Part 3
    print "\nPart 3\n"
    for x in lst:
        prmpt = "Do you like " + x + "? : "
        a = raw_input(prmpt)
        if a == "yes":
            print x.lower()
        elif a == "no":
            lst.remove(x)
            
    print lst
    
    # Part 4
    print "\nPart 4\n"
    print "Original List", lst
    lst2 = lst[::]
    for idx, val in enumerate(lst2):
        lst2[idx] = val[::-1]
    
    print "Modified list", lst2  


if __name__ == "__main__":
    list_lab()