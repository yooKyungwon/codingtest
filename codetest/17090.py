import sys
sys.setrecursionlimit(10000)


r, c = map(int, input().split())
graph = list(list(map(str,input().strip())) for _ in range(r))  #문자가 붙어 있을 땐 strip()사용
visited = list( [0] * c for _ in range(r))
# mark = list( [0] * c for _ in range(r))
#
# print(r, c)
# print(graph)
# print(visited)

def getNextNode(cR, cC) :
    nR, nC = 0, 0
    if graph[cR][cC] == 'U' :
        nR, nC = cR - 1, cC
    elif graph[cR][cC] == 'R' :
        nR, nC = cR, cC + 1
    elif graph[cR][cC] == 'D' :
        nR, nC = cR + 1, cC
    elif graph[cR][cC] == 'L' :
        nR, nC = cR, cC -1
    else  :
        nR, nC = -1,-1
    return nR,nC


def dfs(cR, cC, path) :
    if visited[cR][cC] == 1 : # 방문했던 노드를 또 방문
        for (x, y) in path: # 지금 까지 방문 했던 노드 전부 -1로 변환
            visited[x][y] = -1
        return False
    elif visited[cR][cC] == 2 : #탈출 가능한 경로 에서 부터 시작함
        return True
    elif visited[cR][cC] == -1 :
        return False

    visited[cR][cC] = 1
    path.append((cR,cC))
    nR , nC = getNextNode(cR,cC)

    if nR >= r or nC >= c or nC < 0 or nR < 0:
        for (x, y) in path:
            visited[x][y] = 2
        return True

    result = dfs(nR, nC, path)
    if result:  # 탈출 가능
        for (x, y) in path: # path는 왜있는거지 탈출 가능하면 해당하는 x,y는 툴출 가능한 방문 케이스 기록
            visited[x][y] = 2
    else:  # 탈출 불가
        for (x, y) in path:
            visited[x][y] = -1

    return result

resultCount = 0
for i in range(r) :
    for j in range(c) :
        # visited = list([False] * c for _ in range(r))

        if visited[i][j] == 2 or (visited[i][j] == 0 and dfs(i,j,[])) :
            # mark[i][j] = True
            resultCount +=1

# print(mark)
print(resultCount)
