import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

N, M= map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# print(visited)


def bfs () :
    q = deque([(0,0)])
    cheese = deque([])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    contact = [[0] * M for _ in range(N)]  # 치즈와 외부 공기 접촉 횟수 기록
    visited[0][0] = 1
    # for item in visited :
    #     print(item)
    # ox = -1
    # oy = -1

    while(q) :
        cx, cy = q.popleft()
        # print(cx, cy)

        for i in range(0, 4):
            # print(i)
            nx = cx + dx[i]
            ny d= cy + dy[i]
            # print( visited[nx][ny])

            if  0 <= nx < N  and 0 <= ny < M and visited[nx][ny] == 0  :


                if graph[nx][ny] == 0 :
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif graph[nx][ny] == 1 :  # 1인 값이 있는 곳에 이동 하지 않음
                    print(nx, ny)
                    contact[nx][ny] += 1   # 0에서 1을 발견한 횟수

    for i in range(N):
        for j in range(M):
            if (graph[i][j] == 1 and contact[i][j] >= 2):
                cheese.append((i, j))

    print(cheese)

    for x, y in cheese :
        graph[x][y] = 0
    # for item in graph :
    #     print(item)
    return len(cheese)

def countCheese () :
    cheeseCount = 0
    for x in range(0, N):
        for y in range(0, M):
            if (graph[x][y] == 1) :
                cheeseCount +=1
    return cheeseCount




cheeseCount = countCheese()
count = 0;
while (True) :
    removedcheese = bfs()

    cheeseCount -=removedcheese
    count +=1
    if (cheeseCount ==0) :
        break

print(count)









