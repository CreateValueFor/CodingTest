#총 n가지 종류
#적절히사용해서 가치의 합을 K
#배수이기 때문에 그리디 알고리즘 사용 가능

import sys

input = sys.stdin.readline
N, K = map(int,input().split())
cash_kind = [int(input()) for i in range(N)]
cash_kind.reverse()
# print(cash_kind)
answer = 0

for cash in cash_kind:
    if K == 0:
        break
    answer += K//cash
    K %= cash
print(answer)