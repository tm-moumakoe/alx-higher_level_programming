#!/usr/bin/python3
"""displays value of the X-Request-Id variable found in
the header of the response.
"""


if __name__ == "__main__":
    from requests import get

    doc = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print("\t- type: {}".format(doc.text.__class__))
    print("\t- content: {}".format(doc.text))
