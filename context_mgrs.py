"""

Together with the 'with' keyword, context managers are constructs that allows you to perform automatic operations
(such as opening and closing a file)

"""
from contextlib import contextmanager

@contextmanager
def file_open(file_path):
    try:
        f_obj = open(file_path, 'w')
        yield f_obj
    except OSError:
        print("Error")
    finally:
        print("Closing file")
        f_obj.close()

with file_open('C:\\Users\shay.elmualem\Desktop\WAF_RULES_MODES_377077_01-22-2017.csv') as fobj:
    fobj.write('shay test')


# contextlib closing

# We could do:

@contextmanager
def closing_func(db):
    try:
        yield db.conn()
    finally:
        db.close()

# or even easier - this will close the web page once the with statement ends
from urllib.request import urlopen
from contextlib import closing

with closing(urlopen('http://www.google.com')) as my_page:
    for line in my_page:
        print(line)



# additional context manager that exist in contextlib is called supress:
# it will supress any number of exceptions raised

from contextlib import suppress

with suppress(FileNotFoundError):
    with open("file_that_does_not_exist.txt", 'r') as no_file:
        for line in no_file:
            print(line)

# exception easily supressed, literally :)

# contextmanagers are awesome

# stdout / stderr example, without contextlib

import sys
path = 'C:\\Users\shay.elmualem\Desktop\WAF_RULES_MODES_377077_01-22-2017.csv'
with open(path, 'w') as fobj:
    sys.stdout = fobj
    help(sum)

# stdout / stderr example with contextlib

from contextlib import redirect_stdout

path = 'C:\\Users\shay.elmualem\Desktop\WAF_RULES_MODES_377077_01-22-2017.csv'
with open(path, 'w') as fobj:
    with redirect_stdout(fobj):
        help(redirect_stdout)



