#!/usr/bin/python3
cap = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - cap)), end="")
    cap = 32 if cap == 0 else 0
