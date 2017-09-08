"""
Counter, dict subclass, can be used in counting objects, elemnts counted are
stored as dict keys and their count
value is the dict value.

Some key methods:

'most_common', 'subtract', 'elements'

"""

from collections import Counter

__author__ = "wowshay@gmail.com"

counter = Counter('superfluous')

print(counter['s'])

print(type(counter))

print(list(counter.elements()))
print(set(counter.elements()))

print(counter.most_common(2))

counter_one = Counter('encyclopedia')
counter_two = Counter('pedia')
print(counter_one)
counter_one.subtract(counter_two)
print(counter_one)


counter_abc = Counter('aabbccddeeffgghhiijjkkllmmnnoopppppp')
abc_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
print("Counter:", counter_abc)
counter_abc.subtract(abc_list)
print(counter_abc)