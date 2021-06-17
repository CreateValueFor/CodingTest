import copy 
def solution(triangle):
    answer = 0
    dp = copy.deepcopy(triangle)
    #dp테이블 생성하기
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            dp[i][j] = 0
    dp[0][0] = triangle[0][0]
    print(dp)
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            prevlen_j = len(triangle) -1
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j==len(triangle[i])-1:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
        print(dp)
    answer = max(dp[len(triangle)-1])
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)