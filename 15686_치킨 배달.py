import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int,input().split())

citymap = [list(map(int,input().split())) for i in range(N)]
chicken_stack = []
house_stack = []
for i in range(N):
    for j in range(N):
        if citymap[i][j] == 2:
            chicken_stack.append([i,j])
        elif citymap[i][j] == 1:
            house_stack.append([i,j])
minv = 9876543210
for ch in combinations(chicken_stack, M):
    sumv = 0
    for home in house_stack:
        sumv += min([abs(home[0]-i[0])+ abs(home[1]-i[1])for i in ch])
        if minv <= sumv : break
    if sumv < minv : minv = sumv
print(minv)