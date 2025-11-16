N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()
result = 0


start = 1
end = arr[-1] - arr[0] #끝에서 부터 자른다면

# print(arr, start, end)

while start <= end :
    mid = (end + start) // 2

    current = arr[0]
    count = 1
    for i in range(1, N):
        if abs(arr[i] - current) >= mid:
            current = arr[i]
            count += 1

    if  count >= M :
        start = mid + 1
        result = mid
    else :
        end = mid - 1

print(result)