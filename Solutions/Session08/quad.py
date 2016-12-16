
class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __call__(self, x):
        return self.a * x**2 + self.b * x + self.c


#my_quad = Quadratic(a=2, b=3, c=1)