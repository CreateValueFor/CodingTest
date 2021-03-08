
# N*M사이즈의 종이, 각각의 칸에 정수가 하나씩 쓰여 있음
#테트로미노 하나를 적절히 놓아 테트로미노가 놓인 칸에 쓰여 있는 수들의 
#합을 최대로 하는 프로그램
#회전 대칭 가능
#테트로미노 구현 방법

#논의하고 싶은 것
#벡터로 생각, 4번 가는동안  테트로미노가 정사각형 4개로 구현가능한 모든 도형 표현
#각각의 정사각형에서 어느 곳으로 가는 것이 제일 숫자가 큰지 계산
import sys

#필드
sum = 0 #숫자들의 합
coordinate_group = [] #선택된 점들의 좌표

x,y = input().split()
x = int(x)
y = int(y)
plate = []


#입력 처리부 판 생성 
for i in range(x):
    tmp = sys.stdin.readline()
    # n += tmp.count('0')
    plate.append((tmp.replace('\n','').split()))
plate_int = []
for line in plate:
    plate_int.append(list(map(int,line)))
# print(plate_int)

tetromino = [
    [(0,0), (0,1), (1,0), (1,1)], 
    [(0,0), (0,1), (0,2), (0,3)], 
    [(0,0), (1,0), (2,0), (3,0)], 
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], 
    [(0,0), (0,1), (0,2), (1,2)], 
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], 
    [(1,0), (1,1), (1,2), (0,1)], 
    [(0,0), (1,0), (2,0), (1,1)], 
    [(1,0), (0,1), (1,1), (2,1)], 
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

    
def find(x,y):
    global sum
    for i in range(len(tetromino)):
        tmp_sum = 0
        for j in range(4):
            try:
                next_candidate_x = x + tetromino[i][j][0]
                next_candidate_y = y + tetromino[i][j][1]
                tmp_sum += int(plate[next_candidate_x][next_candidate_y])
            except IndexError:
                continue
        sum = max(sum,tmp_sum)

def solve():
    for i in range(x):
        for j in range(y):
            find(i,j)

solve()
print(sum)

#후보를 선택하기 



#입력 예제
# 5 5
# 1 2 3 4 5
# 5 4 3 2 1
# 2 3 4 5 6
# 6 5 4 3 2
# 1 2 1 2 1

# 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# 4 10
# 1 2 1 2 1 2 1 2 1 2
# 2 1 2 1 2 1 2 1 2 1
# 1 2 1 2 1 2 1 2 1 2
# 2 1 2 1 2 1 2 1 2 1



# #사각형에서 최대의 수를 고르는 방향을 찾는 방법
# def find_max(coordinate, plate): #좌표와 판을 인자로 함
#     x, y = coordinate[0], coordinate[1] #x와 y좌표 입력
#     next_candidate = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
#     max = 0
#     voted = []
#     for candidate in next_candidate:
#         if max < plate[candidate[0]][candidate[1]]:
#             max = plate[candidate[0]][candidate[1]]
#             voted = [candidate[0],candidate[1]]
#     return max, voted

# #처음으로 시작할 최대의 수 찾기
# first_coordinate = []
# for line in range(len(plate_int)):