# N*M의 행렬로 표현되는 맵, 1은 이동할 수 없는 벽
# (1,1) 에서 (N,M)의 위치까지 최단경로로 이동하려 
#만약 이동하는 도중에 한개의 벽을 부수고 이동하는것이 좀더 짧다면
#벽을 한개까지 부숴도 됨
#3차원 배열을 만드는데, visit[x][y][i]에서 i가 0이라면 벽을 한번 뚫은 상태이고,
#1이라면 벽을 뚫을 수 있는 상태를 나타낸다.
#bfs을 돌려주는데 벽을 뚫을 수 있는 상태이고, 벽을 만난다면 벽을 뚫어주고 +1을 해준다.
#아직 방문하지 않았고 벽이 아니라면 또한 +1을 해준다.
#너비 우선탐색 알고리즘은 큐로 이용하면 좋다. 시간 복잡도를 위해 덱 사용
import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    q = deque()
    q.append([0, 0, 1])
    visit = [[[0] * 2 for i in range(m)] for i in range(n)]
    visit[0][0][1] = 1
    while q:
        a, b, w = q.popleft()
        if a == n - 1 and b == m - 1:
            return visit[a][b][w]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if s[x][y] == 1 and w == 1:
                    visit[x][y][0] = visit[a][b][1] + 1
                    q.append([x, y, 0])
                elif s[x][y] == 0 and visit[x][y][w] == 0:
                    visit[x][y][w] = visit[a][b][w] + 1
                    q.append([x, y, w])
    return -1
n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, list(input().strip()))))
print(bfs())