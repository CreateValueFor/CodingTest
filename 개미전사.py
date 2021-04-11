import sys

input = sys.stdin.readline

N = int(input())
container = list(map(int, input().split()))
d = [0] * 100
d[0] = container[0]
d[1] = max(container[0], container[1])
for i in range(2,N):
    d[i] = max(d[i-1], d[i-2] + container[i])

print(d[N-1])
