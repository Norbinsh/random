# For fast appends and pops, deque is usually better, for the fast random 
# access, lists are still better

from collections import deque, defaultdict
import string

d = deque([number for number in range(1,20+1)])
print(d)

d.appendleft(0)
print(d)

#rotate back and forth, remove and return to original state 

d.rotate(1)
print(d)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)
d.rotate(-1)
print(d)
d.remove(0)
print(d)

# trying with file, will create a file then read recent lines from it, similiar 
# to linux's tail method 

with open('deque_file.txt', 'w') as output_file:
	try:
		for item in d:
			output_file.write(str(item)+'\n')
	except OSError:
		print("issue writing to file")


with open('deque_file.txt', 'r') as input_file:
	print(deque(input_file, 10))



