#https://www.acmicpc.net/problem/19542
import sys
input = sys.stdin.readline # 중요 해당 코드가 없으면 시간에러 발생
sys.setrecursionlimit(10 ** 9)

def DFS(S, pre) :
    global ans
    check = 0
    for i in graph[S] :
        if i != pre :
            check = max(check, DFS(i, S))
    if check >= D :
        ans += 1
    return check + 1



N,S,D = map(int, input().split())
graph = [ [] for _ in range(N + 1)] # 1부터 시작

for i in range(N - 1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


ans = 0
DFS(S, 0)
print(max(0, 2 * (ans-1)))
