"""
ordereddict, subclass of dict that keeps trac of the order of the keys, as they
are added.
can be sorted() or reversed(). 
In addition, it checks for both equality AND its order!

New methods in python3 includs popitem and move_to_end, that do what their 
name implies ;)
"""
from collections import OrderedDict

standard_dict = {'a':'1', 'b':'2', 'c':'3', 'd':'4'}
print(standard_dict) # random every time


ordered_d = OrderedDict(sorted(standard_dict.items()))

print(ordered_d) # will remain the sorted order 

# ordereddict supports reverse 
for key in reversed(ordered_d):
	print(key)


# let's try to use the new methods 

# popitem

ordered_d.popitem()
print(ordered_d) # removes the last item. always the same once since it's sorted

ordered_d.move_to_end('a')
print(ordered_d) # now 'a' is the last (most right) item in the dict even though 
# it is sorted, good times! 




