import copy
import  sys
from collections import deque
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

dx = [1, -1 , 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
graph = []

for i in range(N) :
    graph.append(list(map(int, input().split())))



def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)

    for i in range(N) :
        for j in range(M) :
            if tmp_graph[i][j] == 2 :
                queue.append((i,j))

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                continue
            if tmp_graph[nx][ny] == 0 :
                tmp_graph[nx][ny] = 2
                queue.append((nx,ny))
    global answer
    cnt = 0

    for i in range(N) :
        cnt += tmp_graph[i].count(0)
    answer = max(answer, cnt)



def makeWall(cnt) :
    if cnt == 3 :
        bfs()
        return

    for i in range(N) :
        for j in range(M) :
            if graph[i][j] == 0 :
                graph[i][j] = 1
                makeWall(cnt + 1)
                graph[i][j] = 0


answer = 0
makeWall(0)
print(answer)
