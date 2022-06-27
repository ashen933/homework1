import math


def zeros(n):
    a = 0
    if n == 0:
        pass
    else:
        while n > 0:
            n //= 5
            a += n
    print(a)
    return int(a)


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
