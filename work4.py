def bananas(s, word='banana') -> set:
    result = []

    if word == '':
        result.append(''.rjust(len(s), '-'))
        return result

    lefts = ''
    for i in range(len(s)):
        if word[0] == s[i]:
            lefts = ''.rjust(i, '-') + s[i]
            if s[i + 1:] == '' and word[1:] == '':
                result.append(lefts)
            else:
                rlist = bananas(s[i + 1:], word[1:])
                for rights in rlist:
                    result.append(lefts + rights)
    return set(result)
