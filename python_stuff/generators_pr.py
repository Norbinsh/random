# http://dabeaz.com/coroutines/Coroutines.pdf


def countdown(n):
    print("Counting down from", n)
    while n > 0:
        yield n
        n -= 1

x = countdown(10)

print(x.__next__())
print(x.__next__())
print(x.__next__())

"""
Output:
Counting down from 10
10
9
8

When the generator returns, iteration stops:

Traceback (most recent call last):
    print(x.__next__())
StopIteration

"""

example_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4}


def pop_the_dict(the_dict=None):
    while True:
            pop = the_dict.popitem()
            yield pop
try:
    for key in pop_the_dict(the_dict=example_dict):
        print(key)
except KeyError:
    print("dict is empty")

# 11 / 99



