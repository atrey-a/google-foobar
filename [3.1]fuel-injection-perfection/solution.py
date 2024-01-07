def solution(n):
    n = int(n)
    a = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
            a += 1
        elif n == 3 or n % 4 == 1:
            n -= 1
            a += 1
        else:
            n += 1
            a += 1
    return a

if __name__ == '__main__':
    assert (solution('15') == 5)
    assert (solution('4') == 2)
