#!/usr/bin/env python3

import sys
import socket
from collections import namedtuple
from concurrent.futures import ThreadPoolExecutor

RESULT = namedtuple('Result', ['address', 'port80', 'port443'])

def check(address):
    with socket.socket() as sock1, socket.socket() as sock2:
        try:
            sock1.connect((address, 80))
        except:
            P80 = False
        else:
            P80 = True
        try:
            sock2.connect((address, 443))
        except:
            P443 = False
        else:
            P443 = True

    return RESULT(address, P80, P443)


def main(urls):
    with ThreadPoolExecutor(max_workers=10) as pool:
        results = pool.map(check, urls)
        for result in results:
            print(result)

if __name__ == '__main__':
    # urls = sys.argv[1:]
    urls = ["www.google.com", "www.ynet.co.il", "www.shay.host"]
    main(urls)
    sys.exit(0)

# call script with ./scan80_443.py google.de heise.de golem.de serversupportforum.de
