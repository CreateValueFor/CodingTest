# 100,000 이하이기 때문에 NlogN알고리즘 설계를 계획
# python 내장 sort 알고리즘이 n log n
# 절댓값을 기준으로 sort 해주고 합친게 작은 값 찾기
# 부호가 모두 같은 경우는 가장 작은 값 찾기
import sys

input = sys.stdin.readline
num = int(input())

num_list = list(map(int,input().split()))
num_list.sort(key = lambda a : abs(a))
minVal = 20000000001
start = 0
end = 0
for i in range(len(num_list)-1):
    comb = num_list[i+1] + num_list[i]
    if abs(comb) < minVal :
        minVal = abs(comb)
        start = i
        end = i+1

if num_list[start] < num_list[end]:
    print(num_list[start],num_list[end])
else:
    print(num_list[end], num_list[start])
