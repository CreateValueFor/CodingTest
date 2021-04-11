import sys
input = sys.stdin.readline

K, N = map(int,input().split())
wire = [int(input()) for i in range(K)]

start= 1; end = max(wire)

result = 0
while start <= end:
    mid = (start + end)//2
    count = 0
    
    for w in wire:
        count += w//mid
    if count >= N:
        start = mid+1
        result = mid
    else :
        end = mid-1
print(result)