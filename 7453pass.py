import sys
input = sys.stdin.readline
#in함수는 전부 순회하기 때문에 try except 사용
def solution(N) :
    answer = 0
    A, B, C, D = [], [] ,[] ,[]
    #4개의 리스트에 각각의 값들을 대입
    for _ in range(N) : 
        a1,b1,c1,d1 = map(int, input().split())
        # ; 표시로 여러개를 한번에 쓸 수 있음
        A.append(a1); B.append(b1); C.append(c1); D.append(d1)
    #A+B = - (C+D)를 이용할 수 있도록 딕셔너리 생성
    candidate = dict()
    #A와 B의 합으로 만들어 질 수 있는 모든 조합 딕셔너리에 키 저장
    for i in range(N) :
        for j in range(N) :
            tmp = A[i] + B[j]
            if tmp in candidate :
                candidate[tmp] += 1
            else :
                candidate[tmp] = 1
    #C와 D의 합으로 만들어 질 수 있는 조합들이 각각 딕셔너리에 존재하는지 탐색
    for i in range(N) :
        for j in range(N) :
            tmp = -(C[i] + D[j])
            if tmp in candidate :
                answer += candidate[tmp]

    return answer

if __name__ == "__main__":
    n = int(input())
    print(solution(n))


#6
# -45 22 42 -16
# -41 -27 56 30
# -36 53 -37 77
# -36 30 -75 -46
# 26 -38 -10 62
# -32 -54 -6 45