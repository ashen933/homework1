import math


def zeros(n):
    a = 0
    if n == 0:
        pass
    else:
        for i in range(1, int(math.log(n, 5)) + 1):
            a += n / 5**i

    return int(a)


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
