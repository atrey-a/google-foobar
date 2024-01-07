def solution(l):
    l = sorted(l)
    r = [x%3 for x in l]
    s = sum(r)%3
    if s!=0:
        pos = -1
        for i in range(len(r)):
            if r[i] == s:
                pos = i
                break
        if pos == -1:
            pos1 = -1
            for i in range(len(r)):
                if r[i] == (3-s):
                    if pos == -1:
                        pos = i
                    else:
                        pos1 = i
                        break
            if pos1 == -1:
                return 0
            else:
                x, y = l[pos], l[pos1]
                l.remove(x)
                l.remove(y)
        else:
            l.remove(l[pos])
    v = int(''.join(map(str, l[::-1]))) if len(l) > 0 else 0
    return v

if __name__ == '__main__':
    assert (solution([3, 1, 4, 1]) == 4311)
    assert (solution([3, 1, 4, 1, 5, 9]) == 94311)
