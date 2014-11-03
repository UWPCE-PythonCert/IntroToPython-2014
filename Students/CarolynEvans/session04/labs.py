
def dict_lab():
    # 1.
    d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    print d
    d.pop('cake')
    print d
    d.setdefault('fruit', 'Mango')
    print d
    print d.viewkeys()
    print d.viewvalues()
    print 'cake' in d.keys()
    print 'Mango' in d.values()

def dict_zip():
    # 2.
    l = list(range(0,16))
    print l
    print ''

    m = []
    for i in range(16):
        m.append(hex(i))
    print m
    print ''

    d = dict(zip(l,m))
    print d

def dict_tees():
    # 3.
    d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    for key in d.iterkeys():
        d[key] = d[key].count('t')

    print d

def set_lab1():
    s2 = set(range(0,21,2))
    print s2
    s3 = set(range(0,21,3))
    print s3
    s4 = set(range(0,21,4))
    print s4
    print s3.issubset(s2)
    print s4.issubset(s2)

def set_lab2():
    s = set(['P','y','t','h','o','n'])
    s |= {'i'}
    print s

    fs = set(['m','a','r','a','t','h','o','n'])
    print fs
    print 'Union: ', fs.union(s)
    print 'Intersection: ', fs.intersection(s)

def safe_input(label):
    try:
        safeinput = raw_input(label)
        return safeinput
    except:
        return None


def files_lab():
    languages = []
    for student in open('../../../Examples/Session01/students.txt'):
        student = student.strip()
        # Converts student languages to a list.
        # Strips leading spaces and converts to lower case for later grouping.
        studentlanguages = student.split(":")[1].lower().strip()
        languages.extend(studentlanguages.split(","))

    languages.remove('languages')

    # Jam packed stagement.
    # Counts the number of occurences of each language string.
    # Ignores keys (languages) that are empty strings or None.
    languagedict = dict((language, languages.count(language)) for language in languages if language)

    for language, kount in languagedict.iteritems():
        print language.strip(), kount


# safeinput = safe_input('Enter here: ')
# print safeinput

files_lab()