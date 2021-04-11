import sys
input = sys.stdin.readline

N, M = map(int, input.split())
house=[int(input()) for _ in range(N)]
house.sort()
start = house[1] - house[0]
end = house[-1] - house[0]

while start <= end:
    mid = (start + end) //2
    first = house[0]
    count = 1
    for i in range(1,N):
        if house[i] >= first+mid:
            count += 1
            first = house[i]
    
    if count >= M:
        start = mid+1
        result = mid
    else:
        end = mid-1
print(result)