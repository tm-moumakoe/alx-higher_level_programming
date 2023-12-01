#!/usr/bin/python3
"""displays value of the X-Request-Id variable found in
the header of the response
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    doc = get(argv[1])
    print(doc.headers.get('X-Request-Id'))
