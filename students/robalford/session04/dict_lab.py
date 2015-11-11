my_dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

print(my_dict)

my_dict.pop('cake')

print(my_dict)

my_dict['fruit'] = 'Mango'

print(my_dict)

for i in my_dict:
    print(i)

print('cake' in my_dict)


print('Mango' in my_dict.values())

new_dict = my_dict.copy()
for i in new_dict:
    new_dict[i] = new_dict[i].count('t')

print(new_dict)

# sets

divisible_by2 = set()
divisible_by3 = set()
divisible_by4 = set()

for i in range(20):
    if i % 2 == 0:
        divisible_by2.add(i)
    if i % 3 == 0:
        divisible_by3.add(i)
    if i % 4 == 0:
        divisible_by4.add(i)

print(divisible_by2, divisible_by3, divisible_by4)

print(divisible_by3.issubset(divisible_by2))
print(divisible_by4.issubset(divisible_by2))


python_set = set()
for chr in 'Python':
    python_set.update([chr])
python_set.update(['i'])
marathon = frozenset(['m', 'a', 'r', 'a', 't', 'h', 'o', 'n'])
print(marathon.union(python_set))
print(marathon.intersection(python_set))
