def solution(prices):
    tmp = []
    
    for i in range(len(prices)):
        count = 0
        for j in range(i+1,len(prices)):
            if i == len(prices)-1:
                break
            count +=1
            if prices[j] < prices[i]:
                break
            # count+= 1
        tmp.append(count)
    return tmp

print(solution([1,2,3,2,3]))