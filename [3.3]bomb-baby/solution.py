def solution(x, y):
    x = int(x)
    y = int(y)
    c = 0
    if not (x >= 1 and y >= 1):
        return "impossible"
    while not (x == 1 and y == 1):
        if (x==1):
            c += y-1
            break
        if (y==1):
            c += x-1
            break
        if (x==y):
            return "impossible"
        elif x>y:
            x, r = x // y, x % y
            if r==0:
                return "impossible"
            c += x
            x = r
        else:
            y, r = y // x, y % x
            if r==0:
                return "impossible"
            c += y
            y = r
    return str(c)

if __name__ == '__main__':
    assert (solution('2', '4') == 'impossible')
    assert (solution('4', '7') == '4')
    assert (solution('2', '1') == '1')
