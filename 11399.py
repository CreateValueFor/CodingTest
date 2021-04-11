#ATM 1대, N명의 사람들 번호가 있음Pi분
import sys
input = sys.stdin.readline

num = int(input())

waiting_list = list(map(int,input().strip().split()))
sorted_list = sorted(waiting_list)
result = 0

for i in range(num):
    tmp_list = sorted_list[:i+1]
    # print(sum(tmp_list))
    result += sum(tmp_list)

print(result)