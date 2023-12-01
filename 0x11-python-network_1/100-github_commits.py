#!/usr/bin/python3
"""displays value of the X-Request-Id variable found in
the header of the response.
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    coms = get(url).json()
    try:
        for i in range(10):
            print("{}: {}".format(
                coms[i].get("sha"),
                coms[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
