#!/usr/bin/python3
"""displays value of the X-Request-Id variable found in
the header of the response.
"""


if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    val = {"email": argv[2]}
    req = Request(argv[1], urlencode(val).encode("ascii"))

    with urlopen(req) as rsp:
        head = rsp.headers.get('X-Request-Id')
        print(rsp.read().decode('utf-8'))
