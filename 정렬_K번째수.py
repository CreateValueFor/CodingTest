def solution(array, commands):
    answer = []
    # print(commands[0])
    for i in commands:
        tmp = array[i[0]-1:i[1]]
        tmp.sort()
        # print(tmp)
        num = tmp[i[2]-1]
        answer.append(num)
    return answer
print(solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]]))