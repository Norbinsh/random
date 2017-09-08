"""
Subclass of python's dict, accepts a default factory such as ints,
lists, but can also accept lambdas for example.
"""

from collections import defaultdict

long_string = "More than just one or a single world can go here here here"

words = long_string.split(' ')

d = defaultdict(int)

for word in words:
    d[word] += 1

print(d, type(d))


# Another example, this time using lists, assigning list of IPs to every
# Domain in the other list.  
domains = ["www.google.com", "www.ynet.com", "www.rekt.org"]
ip_addresses = ['127.0.0.1, 2.2.2.2, 3.3.3.3, 3.3.3.3, 1.2.3.4']

p = defaultdict(list)

for domain in domains:
	p[domain] = ip_addresses

print(p)
