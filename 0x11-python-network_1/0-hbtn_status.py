#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status" using urllib"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as rsp:
        cnt = rsp.read()
        print("Body response:")
        print("\t- type: {}".format(type(cnt)))
        print("\t- content: {}".format(cnt))
        print("\t- utf8 content: {}".format(cnt.decode('utf-8')))
