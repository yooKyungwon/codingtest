#https://www.acmicpc.net/problem/1916
#https://velog.io/@tks7205/다익스트라-알고리즘-with-python

import sys
input = sys.stdin.readline
from collections import deque
import heapq
INF = 1e8

N = int(input())
M = int(input())
list = list(list(map(int, input().split())) for _ in range(M))
distance = [INF] *  (N+ 1)  # value
visited =[False] * (N+1)

start, end = map(int, input().split())

# print(list)
# print(start, end)
#print(" ".join(map(str, solve)))

graph = [[] for _ in  range(N + 1)]

# print(graph)

for data in list :
    # print(data)
    s, d, v = data[0], data[1], data[2]
    graph[s].append((d,v))

# print(graph)

# pq = []                 # 빈 우선순위 큐 생성
# heapq.heappush(pq, 5)   # 값 추가
# heapq.heappush(pq, 1)
# heapq.heappush(pq, 3)
#
# print(heapq.heappop(pq))  # 1 (가장 작은 값)
# print(heapq.heappop(pq))  # 3

def dijkstra(start) :

    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist : # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
            continue

        for i in graph[now] :
            if dist + i[1] < distance[i[0]] : #경유해서 가는길 과 직접 가는길 비교 최소 값이면, # 기존에 입력되어있는 값보다 크다면
                distance[i[0]] =  dist + i[1]
                heapq.heappush(pq, (dist + i[1], i[0]))
dijkstra(start)

print(distance[end])



