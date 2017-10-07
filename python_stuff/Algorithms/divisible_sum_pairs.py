"""
You are given an array of n integers, a0, a1, ... an-1, and a positive integer, k. Find and print the number of (i,j)
pairs where  i < j and ai + aj is evenly divisible by k.
"""

n = 100  # number of integers in the array
k = 22 # pair's sum must be evenly divisible by this

my_string = "43 95 51 55 40 86 65 81 51 20 47 50 65 53 23 78 75 75 47 73 25 27 14 8 26 58 95 28 3 23 48 69 26 3 73 52 34 7 40 33 56 98 71 29 70 71 28 12 18 49 19 25 2 18 15 41 51 42 46 19 98 56 54 98 72 25 16 49 34 99 48 93 64 44 50 91 44 17 63 27 3 65 75 19 68 30 43 37 72 54 82 92 37 52 72 62 3 88 82 71"
#
a = [ int(a_temp) for a_temp in my_string.strip().split(' ')]

b = []

# For each index/value tuple, we'll generate another index value tuple
# Then check if index x and smaller than y, and that both values together are evenly divided.

for x, c in enumerate(a):
    for y, d in enumerate(a):
        if x < y and (c+d) %k == 0:
            b.append([c, d])
print(b)

# Possible list comprehension: b =[[c,d] for x, c in enumerate(a) for y,d in enumerate(a) if x < y and (c+d) %k == 0]




