#+ 그리고 - 만으로 이루어졌다.
# -인 숫자를 제일 크게

import sys

input = sys.stdin.readline

expression = input().strip().replace('+'," + ")
expression = expression.replace('-',' - ')
expression = expression.split()

answer = 0
tmp = 0
is_minus = False
for num in expression:
    if num.isdigit():

        if is_minus:
            tmp+= int(num)
        else:
            answer += int(num)
    else:
        if num =='-':
            is_minus = True
            answer -= tmp
            # print('aa')
            tmp = 0
answer -= tmp
# print(expression)
print(answer)