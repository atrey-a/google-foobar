from itertools import permutations

class Problem:
    def __init__(self, times, times_limit):
        self.times = times
        self.times_limit = times_limit
        self.n = len(self.times)-2

    def reduce(self):
        for p in range(self.n+2):
            for q in range(self.n+2):
                for r in range(self.n+2):
                    if self.times[q][r] > self.times[q][p] + self.times[p][r]:
                        self.times[q][r] = self.times[q][p] + self.times[p][r]

    def check(self):
        for i in range(self.n+2):
            if self.times[i][i] < 0:
                return True
        return False

    def force(self):
        for i in range(self.n+1):
            for perm in permutations(range(1,self.n+1),self.n-i):
                sum = 0
                path = zip([0]+list(perm),list(perm)+[-1])
                for fro, to in path:
                    sum += self.times[fro][to]
                if sum <= self.times_limit:
                    return sorted([x-1 for x in perm])
        return []

    def solve(self):
        self.reduce()
        if self.check():
            return list(range(self.n))
        return self.force()

def solution(times, times_limit):
    problem = Problem(times, times_limit)
    return problem.solve()

if __name__ == '__main__':
    assert (solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3) == [0, 1])
    assert (solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1) == [1, 2])
