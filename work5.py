import functools
import itertools


def count_find_num(primesL, limit):

    pr = functools.reduce(lambda a, b: a * b, primesL)
    d = pr
    c = 0
    while d < limit:
        d *= primesL[0]
        c += 1
    x = range(0, c + 1)
    if c == 0:
        return list()
    lnums = itertools.product(x, repeat=len(primesL))
    snum = set()

    for i in lnums:
        e = pr

        for j in range(len(primesL)):
            e *= primesL[j]**int(i[j])

            if e <= limit:
                snum.add(e)

    return [len(snum), max(snum)]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
