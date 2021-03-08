# 2부터 100개의 도시 
# 1부터 10만개의 버스 
#그래프를 생각한다면 
#너비 우선 탐색 알고리즘
import sys
from collections import deque
INF = sys.maxsize
#저장되는 경로의 순서가 달라질뿐 문제는 없다.
input = sys.stdin.readline
state_num = int(input())
bus_num = int(input())

graph = [[INF for _ in range(state_num +1)]for _ in range(state_num +1)]

for _ in range(bus_num):
    a,b,c = list(map(int,input().strip().split()))
    graph[a][b] = min(c, graph[a][b])

for k in range(1, state_num +1):
    for i in range(1, state_num +1):
        for j in range(1, state_num +1):
            if i==j:
                graph[i][j] = 0
            else:
                graph[i][j] =min(graph[i][j], graph[i][k] + graph[k][j])
for i in range(1,state_num +1):
    for j in range(1,state_num +1):
        if graph[i][j]==INF:#경로가 없을시 0으로
           print(0,end=" ")
        else:
           print(graph[i][j],end=" ")
    print()