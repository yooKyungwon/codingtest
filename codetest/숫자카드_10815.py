import sys
input = sys.stdin.readline

N = int(input())
nList = list(map(int,input().split()))

M = int(input())
mList = list(map(int,input().split()))
solve = [0] * M

# print (N, M, nList, mList)





nList.sort()

#
#
# def checkExist(value, target) :
#     try :
#         idx = mList.index(value)
#     except ValueError :
#         idx = -1
#     return idx == -1

# -10 2 3 6 10

# mid = 2

def find (target) :
    start = 0
    end = N - 1
    while(start <= end) :
        mid = (start + end ) // 2

        if target > nList[mid] :
           start = mid + 1
        elif target < nList[mid] :
            end = mid - 1
        elif target == nList[mid] :
          return target
        else :
          return False


for i in range(M) :
    value =  find(mList[i])
    if not value :
        continue

    if value == mList[i] :
        solve[i] = 1

print(" ".join(map(str, solve)))
