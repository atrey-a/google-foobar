class Explore:
    def __init__(self, map):
        self.map = list(map)
        self.x = len(self.map)-1
        self.y = len(self.map[0])-1
        self.visited_start = self.visit(0,0,1,1)
        self.visited_end = self.visit(self.x,self.y,1,1)

    def visit(self,i,j,val,inc):
        visited = [[0 for n in m] for m in self.map]
        stacc = [[i,j]]
        visited[i][j] = val
        while (len(stacc) > 0):
            val += inc
            stac = list(stacc)
            for point in stac:
                stacc.remove(point)
                if point[0]>0 and self.map[point[0]-1][point[1]]==0 and visited[point[0]-1][point[1]]==0:
                    stacc.append((point[0]-1,point[1]))
                    visited[point[0]-1][point[1]] = val
                if point[1]>0 and self.map[point[0]][point[1]-1]==0 and visited[point[0]][point[1]-1]==0:
                    stacc.append((point[0],point[1]-1))
                    visited[point[0]][point[1]-1] = val
                if point[0]<self.x and self.map[point[0]+1][point[1]]==0 and visited[point[0]+1][point[1]]==0:
                    stacc.append((point[0]+1,point[1]))
                    visited[point[0]+1][point[1]] = val
                if point[1]<self.y and self.map[point[0]][point[1]+1]==0 and visited[point[0]][point[1]+1]==0:
                    stacc.append((point[0],point[1]+1))
                    visited[point[0]][point[1]+1] = val
        return visited

    def solve(self):
        least = (self.x+1)*(self.y+1) if self.visited_start[self.x][self.y] == 0 else self.visited_start[self.x][self.y]
        for i in range(self.x+1):
            for j in range(self.y+1):
                if self.map[i][j]==1:
                    if i>0 and i<self.x and self.visited_start[i-1][j] > 0 and self.visited_end[i+1][j] > 0:
                        if least > self.visited_start[i-1][j] + self.visited_end[i+1][j] + 1:
                            least = self.visited_start[i-1][j] + self.visited_end[i+1][j] + 1
                    if j>0 and j<self.y and self.visited_start[i][j-1] > 0 and self.visited_end[i][j+1] > 0:
                        if least > self.visited_start[i][j-1] + self.visited_end[i][j+1] + 1:
                            least = self.visited_start[i][j-1] + self.visited_end[i][j+1] + 1
        return least

def solution(map):
    problem = Explore(map)
    return problem.solve()

if __name__ == '__main__':
    assert (solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 11)
    assert (solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) == 7)
