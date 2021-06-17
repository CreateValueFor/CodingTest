from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(grid,x,y):
    q = deque()
    q.append((x,y))
    grid[x][y] = 0
    n = len(grid)
    region = []
    while q:
        x, y = q.popleft()
        region.append((x,y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if grid[nx][ny] == 0:
                continue
            if grid[nx][ny] == 1:
                grid[nx][ny] = 0
                q.append((nx,ny))
    return region

def countMatches(grid1, grid2):
    for i in range(len(grid1)):
        grid1[i] = list(map(int,grid1[i]))
        grid2[i] = list(map(int,grid2[i]))
    regions1 = []
    regions2 = []
    for i in range(len(grid1)):
        for j in range(len(grid1)):
            if grid1[i][j] == 1:
                regions1.append(bfs(grid1,i,j))
            if grid2[i][j] == 1:
                regions2.append(bfs(grid2,i,j))
    answer = 0
    for reg1 in regions1:
        for reg2 in regions2:
            if reg1 == reg2:
                answer += 1
    return answer

countMatches(['001','011','100'],['001','011','101'])
