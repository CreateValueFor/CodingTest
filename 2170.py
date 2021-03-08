#수직선
#스위핑 알고리즘 : 어떤 선이나 공간을 한쪽에서부터 쓸어버린다는 것
#겹칠 때와 안 겹칠 때 생각해보기 , 숫자 저장해둬야 함
#안 겹칠 때 그냥 숫자 더하기
#겹칠 때 탐색 후 업데이트(업데이트를 통해 탐색 갯수 줄여주기?)
# 1. 한선분이 다른 선분에 포함
# 2. 두 선분이 겹침
# 3. 선분이 서로 만나지 않음
import sys
input = sys.stdin.readline

num = int(input())
line_list = [tuple(map(int, input().split())) for _ in range(num)]
# print(line_list)

line_list.sort()
# print(line_list)
result = 0
start= end = 0

for tup in line_list:
    if start ==0 and end ==0:
        result = tup[1] - tup[0]
        start, end = tup
        continue

    if start <= tup[0] and end > tup[1]:
        continue

    if end >= tup[0]:
        result += tup[1] - end
        end = tup[1]
        continue

    result += tup[1] - tup[0]
    start,end = tup
print(result)