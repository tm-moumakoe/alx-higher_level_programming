#!/usr/bin/python3
"""displays the value of X-Request-Id variable found in
the header of the response.
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    rsp = get(argv[1])
    if rsp.status_code >= 400:
        print("Error code: {}".format(rsp.status_code))
    else:
        print(rsp.text)
