#!/usr/bin/python3
"""displays value of the X-Request-Id variable found in
the header of the response.
"""


if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from sys import argv

    try:
        with urlopen(argv[1]) as rsp:
            print(rsp.read().decode('utf-8'))
    except HTTPError as err:
        print('Error code:', err.code)
