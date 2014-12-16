__author__ = 'Robert W. Perkins'


def rot_encode(x):
    """Return the Rot 13 coding of x"""
    return x.encode("rot_13")


if __name__ == '__main__':
    print rot_encode('Zntargvp sebz bhgfvqr arne pbeare')
    assert rot_encode(rot_encode('Zntargvp sebz bhgfvqr arne pbeare')) == 'Zntargvp sebz bhgfvqr arne pbeare'
