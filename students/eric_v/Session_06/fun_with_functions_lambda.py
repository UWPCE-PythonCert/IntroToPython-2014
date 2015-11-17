def trapz(fun, a, b, number_of_increments):
    cumulative_increment_area = 0
    for increment in range(number_of_increments):
        lower_boundary = (a + (increment_size(a, b, number_of_increments) * (increment)))
        upper_boundary = (a + (increment_size(a, b, number_of_increments) * (increment + 1)))
        print ('boundaries: ', lower_boundary, upper_boundary)
        local_increment_area = evaluate_increment(fun, lower_boundary, upper_boundary)
        print ('local area: ', local_increment_area)
        cumulative_increment_area += local_increment_area
        print ('cumulative area: ', cumulative_increment_area)
        print("\n")
    return(cumulative_increment_area)

def increment_size(a, b, number_of_increments):
    """
    a is lower function evaluation boundary
    b is upper function evaluation boundary
    """
    increment_width = float((b - a)/number_of_increments)
    print('increment_width: ', increment_width)
    return increment_width

def evaluate_increment(fun, lower_boundary, upper_boundary):
    lower_boundary_height = fun(lower_boundary)
    upper_boundary_height = fun(upper_boundary)
    print ('lower_value = ', lower_boundary_height)
    print ('upper_value = ', upper_boundary_height)
    increment_area = ((lower_boundary_height + upper_boundary_height)/2) * (upper_boundary - lower_boundary)
    return increment_area

#########
# Begin processing
#####################
print (trapz(lambda x: ((x**2) +3), 1, 2, 4))
