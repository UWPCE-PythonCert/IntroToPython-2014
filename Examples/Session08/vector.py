"""
Vector type with +, * redefined as Vector addition and dot product
From Jon Jacky's Intro to Python course:
    http://staff.washington.edu/jon/python-course/
"""


class Vector(list):
    def __repr__(self):
        """
        String representation, uses list (superclass) representation
        """
        return 'Vector(%s)' % super(Vector, self).__repr__()

    def __add__(self, v):
        """
        redefine + as element-wise Vector sum
        """
        assert len(self) == len(v)
        return Vector([x1 + x2 for x1, x2 in zip(self, v)])

    def __mul__(self, v):
        """
        redefine * as Vector dot product
        """
        assert len(self) == len(v)
        return sum([x1 * x2 for x1, x2 in zip(self, v)])

l1 = [1, 2, 3]
l2 = [4, 5, 6]
v1 = Vector(l1)
v2 = Vector(l2)

if __name__ == '__main__':
    print('l1')
    print(l1)
    print('l1 + l2')
    print(l1 + l2)
    # print(l1 * l2) # TypeError
    print('zip(l1, l2)')
    print(zip(l1, l2))
    print('v1')
    print(v1)
    print('v1 + v2')
    print(v1 + v2)
    print('v1 * v2')
    print(v1 * v2)
