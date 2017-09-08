"""
Making use of ChainMap class allowing us to chain together several mappings 
(dictionaries). Faster than creating new dictionary and update()'ing it, so they say.
"""

from collections import ChainMap
import builtins
import argparse
import os

__author__ = "wowshay@gmail.com"

# globals() returns dict of the MODULE namespace
# locals() returns dict of the CURRENT namespace it resides in (function, for example)
# vars() returns dict of CURRENT namespace if no arguments (same as locals()),
# or dict of the argument provided
# vars(args) == args.__dict__


def main():
    app_defaults = {'username':'admin', 'password':'admin'}

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    # print(args.__dict__)
    command_line_arguments = {key:value for key, value in vars(args).items() if value} 
    # using vars with argument
    # here to return a dict type of our existing arguments so we can chain them


    chain = ChainMap(command_line_arguments, os.environ, app_defaults) 
    # Chaining the objects
    print(chain['username']) 
    # Now we can access the items from the same chained object.


if __name__ == '__main__':
    main()
    os.environ['username'] = 'shay'
    main()



