def int32_to_ip(int32):
    a = 1
    b = int32
    c = []
    u = 256
    while a > 0 and b > u:

        a = b % u
        b = b // u
        c.append(str(a))
    c.append(str(b))
    while len(c) < 4:
        c.append('0')
    return '.'.join(c[::-1])


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
