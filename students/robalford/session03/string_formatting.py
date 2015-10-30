# exercise 1
string_1 = "file_{:0>3d} : {:.2f}, {:.0e}".format(2, 123.4567, 10000)
print(string_1)

# exercise 2
values = (2, 4, 6, 8, 10, 12)
num_values = len(values)
values_string = str(values).strip('()')
print("the first {:d} numbers are: {}".format(num_values, values_string))

# exercise 2 revisions

