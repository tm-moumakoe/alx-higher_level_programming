#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    nlist = dir(hidden_4)
    for name in nlist:
        if name[:2] != '__':
            print(name)
