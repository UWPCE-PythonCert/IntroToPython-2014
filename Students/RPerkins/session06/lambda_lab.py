__author__ = 'Robert W. Perkins'


def lam_lab(n):
    l = []
    for i in range(n):
        l.append(lambda x, e=i: x+e)
    return l

if __name__ == '__main__':

    out_lab = lam_lab(10)
    for f in out_lab:
        print f(3)