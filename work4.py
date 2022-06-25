def bananas(s) -> set:
    all = []
    l1 = 6
    l2 = len(s) - l1
    banana_set = set()
    for i in range(1, l2 + 1):
        all.append(list())
        for j in range(len(s)):
            if i == 1:
                st = s
                stl = st[:j] + '-' + st[j + 1:]
                all[i - 1].append(stl)
            else:
                for k in range(len(all[i - 2])):
                    st = all[i - 2][k]
                    stl = st[:j] + '-' + st[j + 1:]
                    all[i - 1].append(stl)
    for i in all:
        banana_set.update(set(i))

    result = set()
    for i in banana_set:
        if i.replace('-', '') == 'banana':
            result.add(i)
    if s == 'banana':
        result.add('banana')
    return result


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {
    "b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
    "-ban--ana", "b-anana--"
}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {
    "ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"
}
