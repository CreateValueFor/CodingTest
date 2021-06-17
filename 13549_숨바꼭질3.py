import sys
from collections import deque

n, k = map(int, input().split())

q = deque()
distance = [-1] * 200001
q.append(n)
distance[n] = 0

while q:
    x = q.popleft()
    if x == k:
        print(distance[x])
        sys.exit()
    if x * 2 <= 200000 and distance[x * 2] == -1:
        distance[x * 2] = distance[x]
        q.appendleft(x * 2)

    if x - 1 >= 0 and distance[x - 1] == -1:
        distance[x - 1] = distance[x] + 1
        q.append(x - 1)

    if x + 1 <= 200000 and distance[x + 1] == -1:
        distance[x + 1] = distance[x] + 1
        q.append(x + 1)