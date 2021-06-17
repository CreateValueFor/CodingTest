def fountainActivation(locations):
    n = len(locations)
    dp = [-1] * (n+1)
    for i in range(1,n+1):
        right = min((i + locations[i-1]),n)
        left = max((i-locations[i-1]),1)
        dp[left] = max(dp[left], right)

    answer = 1
    limit = dp[1]
    newFountain = 0
    for i in range(1,n):
        newFountain = max(newFountain,dp[i])
        if (i == limit):
            answer += 1
            limit = newFountain
    return answer

locations = [0,2,1]
print(fountainActivation(locations))
