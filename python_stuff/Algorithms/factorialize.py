def lets_factor(number):
    if number == 1:
        return 1
    else:
        return number * lets_factor(number - 1)

print(lets_factor(5))
