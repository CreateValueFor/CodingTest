# 한 개의 회의실N개의 회의실에 대한 사용표
import sys

input = sys.stdin.readline
num = int(input())
conference_list = [tuple(map(int, input().strip().split())) for i in range(num)]
#반례계산에 철저하지 못했음
conference_list.sort(key = lambda conference:conference[0])
conference_list.sort(key = lambda conference:conference[1])
result = 0
end = 0
for tup in conference_list:
    if tup[0] >= end:
        result += 1
        end = tup[1]
print(result)