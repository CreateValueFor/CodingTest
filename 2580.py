import sys
#전체 수를 담을 리스트
total = []
#빈칸의 갯수
n = 0 
#문자로 구성된 수 9 개
for i in range(9):
    tmp = sys.stdin.readline()
    n += tmp.count('0')
    total.append(tmp.replace('\n','').split())

total_clear = total
set_a = {'1','2','3','4','5','6','7','8','9'}


#행에서 어떤 숫자가 없는지 검색, 가능한 수를 반환
def row(rows):
    prob = list(set_a -set(total[rows]))
    return prob

#열에서 어떤 숫자가 없는지 검색
def column(columns):
    tmp = []
    for i in total:
        tmp.append(i[columns])
    prob = list(set_a - set(tmp))
    return prob

# 3*3 박스에서 어떤 숫자가 없는지 검색
def box(rows,columns):
    n_row = rows//3 * 3
    n_column = columns//3 * 3
    tmp = []
    for i in range(3):
        for j in range(3):
            tmp.append(total[n_row + i][n_column + j])
    prob = list(set_a - set(tmp))
    return prob

def find_index(total):
    list_zero = []
    for line_index in range(len(total)):
        #0이 존재하는 인덱스에서 검색
        for zero_index in [i for i, value in enumerate(total[line_index]) if value == '0']:
            list_zero.append([line_index,zero_index])
    return list_zero



#모든 라인, backtracking 함수가 재귀가 아님, 재귀함수의 경우 함수를 종료해도 나머지 재귀함수가 더 돌고 있을 수 있음. sys.exit(0) 쓰면 해결 될 수 있음
def backtracking(total):
    # print(find_index(total))
    assign = find_index(total)
    # for line_index in range(len(total)):
    #     #0이 존재하는 인덱스에서 검색
    #     for zero_index in [i for i, value in enumerate(total[line_index]) if value == '0']:
            #가능한 해의 집합
    for location in assign:
        tmp = list(set(row(location[0])) & set(column(location[1])) & set(box(location[0],location[1])))
        tmp_total = total
        if len(tmp) == 1:
            total[location[0]][location[1]] = tmp[0]
        elif len(tmp) > 1:
            for opp in tmp:
                tmp_total[location[0]][location[1]] = opp
                # backtracking(tmp_total)
        # else:





            # elif len(tmp) >1 :
            #     tmp_total = total
            #     for i in tmp:
            #         tmp_total[location[0]][location[1]] = i
            #         tmp_total = backtracking(tmp_total)
            #         if find_index(tmp_total) == True:
            #             tmp_total = total

                    
            # elif len(tmp) ==0:

            
    return total

final = backtracking(total)
for line in final:
    tmp = ""
    for component in line:
        tmp += "{} ".format(component)
    print(tmp)
    