import sys
input = sys.stdin.readline
n = int(input())
adventures = list(map(int,input().split()))
adventures.sort()
print(adventures)

answer = 0

tmp = 0
for i in range(n):
  tmp += 1
  if tmp >= adventures[i]:
    
    answer += 1
    tmp = 0
print(answer)