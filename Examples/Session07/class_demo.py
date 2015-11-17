
class C:
    x = 5

    def __init__(self, y):
        self.y = y

    def meth(self, z):
        C.x = z
        return self.x + self.y + z
