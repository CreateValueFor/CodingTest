import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int,input().split()))
answer = 0

for i in range(n-1,0,-1):
    for j in range(i):
        if num_list[j] > num_list[j+1]:
            answer += 1
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

print(answer)
