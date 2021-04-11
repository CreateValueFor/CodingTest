import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[0]*(N+1) for i in range(N+1)]

dx = [1, 0,-1,0]
dy = [0,-1,0,+1]

apple_num = int(input())

for i in range(apple_num):
    x, y = map(int,input().split())
    #사과 위치는 모두 -1로 바꿔줌
    graph[x][y] = -1
que = deque()
dir_chge_num = int(input())

for i in range(dir_chge_num):
    que.append(input().split())

direction = 0


def turn_right():
    global direction
    direction += 1
    if direction ==4:
        direction = 0
def turn_left():
    global direction
    direction -= 1
    if direction ==-1:
        direction = 3
time = 0
head = [1,1]
tail = [1,1]
tail_direction = []

while True:
    tmp = que[0]
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 1<=nx<= N and 1<= ny <= N:
        if graph[nx][ny] == -1:
            head = [nx,ny]
        else:
            head = []
        if time == tmp[0]:
            que.popleft()
            if tmp[1] == 'D':
                turn_right()
            elif tmp[1] == 'L':
                turn_left()
    time += 1
    
    