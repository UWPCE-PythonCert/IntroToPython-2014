def function_builder(n):
    functions = []
    for i in range(n):
        functions.append(lambda value, increment=i: value + increment)
    return functions
