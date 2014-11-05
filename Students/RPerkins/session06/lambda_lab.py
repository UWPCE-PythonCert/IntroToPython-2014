__author__ = 'Robert W. Perkins'


def lam_lab(n):
    l = []
    for i in range(n):
        l.append(lambda x, e=i: x+e)
    return l


def lam_lab2(num):

    t = []
    [(t.append(lambda x, e=i: x+e)) for i in range(num)]
    return t

if __name__ == '__main__':

    func_outlab = lam_lab(10)
    for f in func_outlab:
        print f(4)

    comp_outlab = lam_lab2(10)
    for g in comp_outlab:
        print g(4)
