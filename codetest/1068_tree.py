#https://www.acmicpc.net/problem/1068
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N = int(input())
listData = list(map(int, input().split()))
parents = list([] for _ in range(N))
deletedNode = int(input())
root = -1

for index, node in enumerate(listData) : #index = child
    # print(index, node)
    if node == -1 :
        root = index
    else :
        parents[node].append(index)


# 루트가 삭제되면 리프 0개
if deletedNode == root:
    print(0)
    sys.exit()

leafCount = 0
def dfs(node2) :
    global leafCount

    if deletedNode == node2 :
        return

    isLeaf = True
    for child in parents[node2] :
        if not deletedNode == child :
            isLeaf = False
            dfs(child)

    if isLeaf :
        leafCount+=1

dfs(root)
print(leafCount)





