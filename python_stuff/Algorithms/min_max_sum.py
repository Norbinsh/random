import sys

a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

value_list = [a,b,c,d,e]
sum_list = [sum(value_list) - item for item in value_list]
print(min(sum_list), max(sum_list))
		

