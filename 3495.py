import sys

input = sys.stdin.readline

height, width = map(int,input().strip().split())
table = [list(input().strip())for _ in range(height)]
answer = 0

for i in range(height):
    is_open = False
    side = 0
    for j in table[i]:
        if '/' ==j or '\\' == j:
            is_open = not(is_open)
            side +=1
        if is_open == True and j == '.':
            answer += 1
    answer += side//2
print(answer)