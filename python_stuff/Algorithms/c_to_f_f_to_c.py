""" Write a program that will convert degrees celsius to degrees fahrenheit. """


def c_to_f(c_t):
    return c_t * 1.8 + 32

print(c_to_f(3))


""" Write a program that will convert degrees fahrenheit to degrees celsius """


def f_to_c(f_t):
    return (f_t - 32) / 1.8

print(f_to_c(40))