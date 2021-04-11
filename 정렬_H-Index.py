def solution(citations):
    answer = 0
    num = len(citations)
    # print(num)
    count_list = [0 for i in range(10001)]
    citations.sort()
    for count in citations:
        count_list[count] += 1
    for i in range(10001):
        if num - count_list[i] < i:
            answer = i
            break
        # print(answer)
        # print(num)
        num -= count_list[i]
        answer = i
    # print(count_list)
    # answer = 0
    return answer
print(solution([3,0,6,1,5]))