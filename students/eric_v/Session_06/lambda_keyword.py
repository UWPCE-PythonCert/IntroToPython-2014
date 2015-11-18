def function_builder(num_of_increments):
    list_of_functions = []
    for increment in range(num_of_increments):
        list_of_functions.append(lambda num_of_increments, up_increment = increment: num_of_increments + up_increment)
    return list_of_functions
