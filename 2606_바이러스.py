import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
line_N = int(input())
graph = {}
for i in range(N+1):
    graph[i] = []
is_virus = [0 for i in range(N+1)]


for i in range(line_N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(x,graph):
    visited = []
    # is_virus[x] = 1
    q = deque()
    q.append(x)

    while q:
        tmp = q.popleft()
        visited.append(tmp)
        for i in graph[tmp]:
            if i not in visited:
                q.append(i)

    return len(visited)-1
print(bfs(1,graph))

