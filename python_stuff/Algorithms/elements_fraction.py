""" Given an array of integers, calculate which fraction of its elements are positive,
which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively.
Print the decimal value of each fraction on a new line. """

arr = [-4, 3, -9, 0, 4, 1]

def get_fraction():

    full = len(arr)
    pos_count = 0
    net_count = 0
    neg_count = 0

    for number in arr:
        if number > 0:
            pos_count += 1
        elif number < 0:
            neg_count += 1
        else:
            net_count += 1
    print(float(pos_count/full))
    print(float(neg_count/full))
    print(float(net_count/full))

get_fraction()
