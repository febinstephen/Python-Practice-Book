class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n-1

    def __iter__(self):
        return self

    def next(self):
        if self.n >= 0:
            i = self.n
            self.n -= 1
            return i
        else:
            raise StopIteration()

y = yrange(5)
x = list(y)
print x
