class Map:
    max_bunnies = 2000000

    def __init__(self, entrances, exits, path):
        self.path = [list(p) for p in path]
        for node in self.path:
            node.insert(0,0)
            node.append(0)
        self.path.insert(0,[0]*(len(self.path)+2))
        self.path.append([0]*(len(self.path)+1))
        self.n = len(self.path)
        for entrance in entrances:
            self.path[0][entrance+1] = self.max_bunnies
        for exit_ in exits:
            self.path[exit_+1][-1] = self.max_bunnies

    def edmonds_karp(self):
        prev = [-1]*self.n
        stacc = [0]
        while len(stacc)>0 and prev[-1] == -1:
            e = stacc[0]
            stacc.remove(e)
            for i in range(self.n):
                if self.path[e][i] > 0 and prev[i] == -1:
                    stacc.append(i)
                    prev[i] = e
        path = []
        e = prev[-1]
        while e != 0:
            if e == -1:
                return None
            path.append(e)
            e = prev[e]
        path.reverse()
        return path

    def solve(self):
        max_flow = 0
        path = self.edmonds_karp()
        while path:
            maxi = self.max_bunnies
            I = 0
            for J in path:
                maxi = min(maxi, self.path[I][J])
                I = J
            max_flow += maxi
            I = 0
            for J in path:
                self.path[J][I] += maxi
                self.path[I][J] -= maxi
                I = J
            path = self.edmonds_karp()
        return max_flow

def solution(entrances, exits, path):
    problem = Map(entrances, exits, path)
    return problem.solve()

if __name__ == '__main__':
    assert (solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]) == 6)
    assert (solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 16)
