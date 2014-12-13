class Animal(object):
    """Generic animal class"""

    def __init__(self, name):
        self.name = name

    def walk(self):
        print ('{} is Walking'.format(self.name))

class Dog(Animal):
    """Man's best friend"""

    def bark(self):
        print('Woof!')
