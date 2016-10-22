class Reverse(object):
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]


def main():
    rev = reversed('My Reversed String')
    for char in rev:
        print(char)

if __name__ == '__main__':
    main()

""" With generators: """

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

def main():
    rev = reverse('My Reversed String')
    for char in rev:
        print(char)

if __name__ == '__main__':
    main()