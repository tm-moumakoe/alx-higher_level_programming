#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        ret = fct(*args)
        return ret
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
