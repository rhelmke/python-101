import re


def sample_one(i):
    a = ""
    t = i.split(".")
    if len(i) > 1:
        a = t[-1]
    b = ".".join(t[0:-1])
    c = re.search(r"-([0-9]+)\Z", b)
    if c is not None:
        c = int(c.group(1)) + 1
        n = re.sub(r"-([0-9]+)\Z", "-{}".format(c), b)
    else:
        n = b + "-1"
    return n + "." + a
