import sys
input = sys.stdin.readline

text = input()
x = len(text)
candidate_len = list(range(2499,0,-2))
if x % 2 == 1:
    y = x//2 +1
else:
    y = x //2 + 1
candidate_len = candidate_len[-1:-y:-1]
candidate_len.reverse()
for length in candidate_len:
    print(length)
    if length != 1:
        mid_plus = length//2 
        tmp = []
        for i in range(x - length):# while문으로 수정
            print(text[i:i+mid_plus],text[i+length-mid_plus:i+length][::-1])
            # print(text[i+length:i+mid_plus:-1])
            if text[i:i+mid_plus]== text[i+length-mid_plus:i+length][::-1]:
                tmp.append(range(i:i+length))