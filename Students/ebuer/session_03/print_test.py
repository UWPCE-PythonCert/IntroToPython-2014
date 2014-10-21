

client_list = [
    (('Askew', 'Anne'), (87.50, 100, 200)),
    (('Bocher', 'Joan'), (25, 43.27)),
    (('Clarkson', 'Jeremy'), (10.03,)),
    (('Hamont', 'Matthew'), (1000, 250, 5)),
    (('May', 'James'), (30, 75)),
    (('Parris', 'George van'), (25, 35, 45))]


def person_len(person):
    l = 0
    for p in person:
        l += len(p)
    return l


#make a name list and a money list
def list_maker(client_list):
    donors = []
    donations = []
    for person in client_list:
        donors.append(person[0])
        donations.append(person[1])
    return donors, donations

donors, donations = list_maker(client_list)

#find max person name length
name_length_value = 0
for d in donors:
    if person_len(d) > name_length_value:
        name_length_value = person_len(d)

name_length_value += 5   # need to add some space after the name


print '{0: >{l}}'.format(' ',l=name_length_value),
print '{a: >8}  {b: >8}  {c: >8}    {d: >8}'\
        .format(a='Num', b='Total', c='Avg', d='Donations')

for person in donors:
    i = donors.index(person)
    #print '{f} {l}'.format(f=person[1], l=person[0]),

    l = len(donations[i])
    avg_d = 0
    tot_d = 0
    d_list = []     # d-listed, hilarious
    c_list = []


    for d in donations[i]:
        avg_d += d / l
        tot_d += d
        d_list.append(d)

        cwidth = 10 - len(str(d))
        c_list.append(cwidth)

    name_str = '{first} {last}'.format(first=person[1], last=person[0])
    print '{name_str: <{l}}'.format(name_str=name_str, l=name_length_value),
    print '{l: >8d}  {tot_d: >8.2f}  {avg_d: >8.2f}  '\
        .format(l=l, tot_d=tot_d, avg_d=avg_d),

    d_list.sort(reverse=True)

    for d in d_list:
        print '{d: >8.2f}'.format(d=d),

    print '\n'


