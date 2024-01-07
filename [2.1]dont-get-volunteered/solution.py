class Chessboard:
    def __init__(self,src,dest):
        self.visited = [False for i in range(64)]
        self.queue = [src]
        self.counter = 0
        self.dest = dest
        if dest != src:
            self.search()

    def itc(self,V):
        return V%8, V//8

    def cti(self,X, Y):
        return Y*8+X

    def horse(self,X, Y, id):
        if id==0:
            return X-2, Y-1
        elif id==1:
            return X-2, Y+1
        elif id==2:
            return X+2, Y-1
        elif id==3:
            return X+2, Y+1
        elif id==4:
            return X-1, Y-2
        elif id==5:
            return X-1, Y+2
        elif id==6:
            return X+1, Y-2
        elif id==7:
            return X+1, Y+2

    def search(self):
        self.counter += 1
        copy_q = list(self.queue)
        for start in copy_q:
            self.visited[start] = True
            self.queue.remove(start)
            for i in range(8):
                x, y = self.itc(start)
                X, Y = self.horse(x, y, i)
                if (0<=X<=7) and (0<=Y<=7):
                    N = self.cti(X,Y)
                    if not self.visited[N]:
                        if N == self.dest:
                            return
                        else:
                            self.queue.append(N)
        self.search()

    def answer(self):
        return self.counter

def solution(src, dest):

    searcher = Chessboard(src,dest)
    return searcher.answer()

if __name__ == '__main__':
    assert (solution(19,36) == 1)
    assert (solution(0,1) == 3)
