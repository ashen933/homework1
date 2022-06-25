def domain_name(url):
    a = url.split('//')
    b = ''
    c = ''
    if len(a) == 2:
        b = a[1]
    else:
        b = a[0]
    b = b.split('www.')
    if len(b) == 2:
        c = b[1]
    else:
        c = b[0]
    d = c.split('.')[0]
    return d


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
