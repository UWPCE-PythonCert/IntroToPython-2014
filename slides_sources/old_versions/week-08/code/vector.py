"""
Vector type with +, * redefined as vector addition and dot product
From Jon Jacky's Intro to Python course:
    http://staff.washington.edu/jon/python-course/
"""


class vector(list):
    def __repr__(self):
        """
        String representation, uses list (superclass) representation
        """
        return 'vector(%s)' % super(vector, self).__repr__()

    def __add__(self, v):
        """
        redefine + as element-wise vector sum
        """
        assert len(self) == len(v)
        return vector([x1 + x2 for x1, x2 in zip(self, v)])

    def __mul__(self, v):
        """
        redefine * as vector dot product
        """
        assert len(self) == len(v)
        return sum([x1 * x2 for x1, x2 in zip(self, v)])

l1 = [1, 2, 3]
l2 = [4, 5, 6]
v1 = vector(l1)
v2 = vector(l2)

if __name__ == '__main__':
    print 'l1'
    print l1
    print 'l1 + l2'
    print l1 + l2
    # print l1 * l2 # TypeError
    print 'zip(l1, l2)'
    print zip(l1, l2)
    print 'v1'
    print v1
    print 'v1 + v2'
    print v1 + v2
    print 'v1 * v2'
    print v1 * v2
