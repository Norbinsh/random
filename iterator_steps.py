from itertools import islice


class Steps:
    def __init__(self, data, nsteps):
        self.data = data
        self.nsteps = nsteps
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= (len(self.data)):
            raise StopIteration
        current = self.data[self.index]
        self.index = self.index + self.nsteps
        return current


my_data = Steps("Iterators", 2)
it = iter(my_data)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


for v in islice('Iterators', 0, None, 2):
    print(v)