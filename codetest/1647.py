#https://www.acmicpc.net/problem/1647
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []

for _ in range(M) :
    a, b, c = map(int, input().split())
    edges.append((c, a, b)) # (cost, start, end)

# print("before : " , edges)
edges.sort()

# print ("after : " , edges)

#union-find 구현
parent = list(range(N + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b) :
    a = find(a)
    b = find(b)
    if a== b:
        return False # 같은 집합 -> 사이클 발생
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
    return True

total_cost = 0
max_edge = 0

#Kruskal
for cost, a, b in edges:
    if union(a, b) :
        total_cost += cost
        if cost > max_edge :
            max_edge = cost

# 가장 비싼 간선 하나 잘라서 두 마을로 분리
print(total_cost - max_edge)