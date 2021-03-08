#1. ABCD 4개의 배열중 2개를 선택하여 합의 값을 알아낸다.(필자는 A,B를 선택)

#2. 1에서 알아낸 값을 dict에 저장한다. key : 합의 값, Value : 나온 횟수 (추후 시간복잡도를 줄이기 위해)

#3. 1에서 선택한 배열 이외의 나머지 2개 배열에 대해서 합의 값을 알아낸다.

#4. 3에서 구한 값이 dict에 있다면 정답에 해당 value 값을 더한다.

import sys 
n = int(sys.stdin.readline()) 
alist, blist, clist, dlist = [], [], [], [] 
for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split()) 
    alist.append(a); blist.append(b); clist.append(c); dlist.append(d) 
    
ab, cd = {}, {} 
for a in alist: 
    for b in blist: 
        if not ab.get(a+b): #여기서 문제가 되었을 듯 함
            ab[a+b] = 1 
        else: ab[a+b] += 1 

for c in clist: 
    for d in dlist:
        if not cd.get(c+d): 
            cd[c+d] = 1 
        else: 
            cd[c+d] += 1 

ans = 0 

for _, key in enumerate(ab): 
    if cd.get(-key):
        ans += (ab[key] * cd[-key]) 

print(ans)


# if __name__ == "__main__"
#파이썬 인터프리터가 모듈을 실행하게 될때는 7453.py로 namespace를 
#갖지 않고 __main__이라는 namespace로 간줗아ㅕ 다루게 된다.
# 따라서 위 말은 만일 이 파일이 인터프리터에 의해서 실행되는 경우라면
#이라는 의미를 갖는다. 따라서 인터프리터에 의해 직접 실행될 경우에만
#실행하도록 하고 싶은 코드 블록이 있는 경우에 사용한다.
