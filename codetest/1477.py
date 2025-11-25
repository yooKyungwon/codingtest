#https://www.acmicpc.net/problem/1477
import sys

N, M, L = map(int, input().split())  # R, C, L
list = [0] + list(map(int, input().split())) + [L]
list.sort()
# print(list)

def upper() :
    start = 1
    end = L - 1
    result = 0


    while start <= end :
        count = 0
        mid = (start + end) // 2
        for i in range(1, len(list)) :
            if list[i] - list[i - 1] > mid:
                # 나눈 만큼 휴게소를 설치 (현재 설치 돼있는 구역은 제외해야해서 -1)
                count += (list[i] - list[i - 1] - 1) // mid

        if count > M :
            start = mid + 1
        else :
            end = mid - 1
            result = mid

    return result

print(upper())
