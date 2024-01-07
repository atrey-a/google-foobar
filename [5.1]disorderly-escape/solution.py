from math import factorial
from collections import Counter

class Problem:
    def __init__(self,w,h,s):
        self.w = w
        self.h = h
        self.s = s

    def gcd(self,a,b):
        while b != 0:
            a,b = b,a%b
        return a

    def count_partition(self,C,N):
        count = factorial(N)
        for x,n in Counter(C).items():
            count //= (x**n)*factorial(n)
        return count

    def traverse_possible_partns(self, n, i):
        yield [n]
        for i in range(i,(n//2)+1):
            for p in self.traverse_possible_partns(n-i,i):
                yield [i] + p

    def solve(self):
        grid = 0
        for cpw in self.traverse_possible_partns(self.w,1):
            for cph in self.traverse_possible_partns(self.h,1):
                m = self.count_partition(cpw, self.w)*self.count_partition(cph,self.h)
                grid += m*(self.s**sum([sum([self.gcd(i, j) for i in cpw]) for j in cph]))
        return grid//(factorial(self.w)*factorial(self.h))

def solution(w,h,s):
    problem = Problem(w,h,s)
    return str(problem.solve())

if __name__ == '__main__':
    assert (solution(2, 3, 4) == '430')
    assert (solution(2, 2, 2) == '7')
