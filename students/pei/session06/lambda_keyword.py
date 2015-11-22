#n = 3

def function_builder(n):
    func_list = []
    for i in range(n):
        func_list.append(lambda x, y=i: x+y)
        print (i)
    return (func_list)


















