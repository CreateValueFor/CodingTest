import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

t = int(input())
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for i in range(n+1)]
    distance = [INF] * (n+1)
    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a,s))
    dijkstra(c)
    count = 0
    max_time = 0
    for d in distance:
        if d != INF:
            count += 1
            max_time = max(d, max_time)
    print(count, max_time)