#https://www.acmicpc.net/problem/17090
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 0 no 방문 2는 탈출 가능  1은 방문 했던것

r, c = map(int, input().split())
graph = list(list(map(str,input().strip())) for _ in range(r))  #문자가 붙어 있을 땐 strip()사용
visited = list( [0] * c for _ in range(r))
# mark = list( [0] * c for _ in range(r))
#
# print(r, c)
# print(graph)
# print(visited)

def getNextNode(c) :
    cR, cC = c
    nR, nC = c

    if graph[cR][cC] == "U" :
        nR = cR - 1
    elif graph[cR][cC] == "R":
        nC = cC + 1
    elif graph[cR][cC] == "D" :
        nR = cR + 1
    elif graph[cR][cC] == "L":
        nC = cC - 1

    return (nR, nC)

def dfs(S) :
    cR, cC = S
    if visited[cR][cC] == 1 :
        visited[cR][cC] = -1
        return False
    elif visited[cR][cC] == 2 :
        return True
    elif visited[cR][cC] == -1 :
        return False

    visited[cR][cC] = 1

    nR, nC = getNextNode((cR, cC))
    if nR < 0 or nC < 0 or nR >= r or nC >= c :
        visited[cR][cC] = 2
        return True
    result = dfs((nR,nC))

    if result :
        visited[cR][cC] = 2
    else:
        visited[cR][cC] = -1
    return result

resultCount = 0

for i in range(r) :
    for j in range(c) :
        if dfs((i,j)) :
            resultCount += 1

print(resultCount)
