"""
Basic usage of the argparse library, with short, long options, and a mutually exclusive group, that tells us
if two or more of the group's arguments may not be used together.
Also feeding type with a custom function to check for the provided argument type and in my case, range.
"""

import argparse

__author__ = "wowshay@gmail.com"


def check_int_range(val):
    val = int(val)
    if val <= 1900 and val <= 10**5:
        return val
    else:
        raise argparse.ArgumentTypeError("{} is not <= 1900 <= {}".format(val, (10**5)))


def get_initial_args():
    """ Getting the year argument to be used in a different function.
    Performing a int type and range check for the year argument """
    parser = argparse.ArgumentParser(description="Collecting the year to be checked in our script",
                                     epilog="leap_year -y 2005")

    # Creating new group that'll have exclusive arguments!
    new_group = parser.add_mutually_exclusive_group()
    new_group.add_argument('-a', help="can't be used with argument 'b'", action='store')
    new_group.add_argument('-b', help="can't be used with argument 'a'", action='store')

    parser.add_argument('-y', '--year', type=check_int_range, action='store', required=True,
                        help='Enter the year you want to check, must be <= 1900 <= 10**5')
    parser.add_argument('-u', '--useless', default=False, help="No need for this one really")

    args = parser.parse_args()
    return args

# argparse_a.py: error: argument -b: not allowed with argument -a


def leap_check():
    """ Simple test to see whether it's a leap year or not """
    args = get_initial_args()
    leap = False
    if args.year % 4 == 0 and (args.year % 100 != 0 or args.year % 400 == 0):
        leap = True
    return leap


if __name__ == '__main__':
    print(leap_check())
