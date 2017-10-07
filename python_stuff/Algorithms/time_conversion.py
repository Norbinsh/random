import re

time = input().strip()

def validate_input(string_to_validate):
	if re.match(r'^(1[0-2]|0[1-9]):([0-5][0-9]):([0-5][0-9])([AP]M)$', string_to_validate):
		return True
	else:
		return False

def time_converter(string_to_convert):
	if string_to_convert.split(':')[0] == '12' and "AM" in string_to_convert:
		print(string_to_convert.replace(string_to_convert.split(':')[0], '00', 1).strip("AM"))
	elif string_to_convert.split(':')[0] == '12' and "PM" in string_to_convert:
		print(string_to_convert.strip("PM"))
	elif "PM" in string_to_convert:
		print(string_to_convert.replace(string_to_convert.split(':')[0], 
			str(int(string_to_convert.split(':')[0])+12), 1).strip("PM"))
	else:
		print(string_to_convert.strip("AM"))

if validate_input(time):
	time_converter(time)

