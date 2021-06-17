def fountainActivation(locations):
    n = len(locations)
    dp = [-1] * n

    for i in range(n):
		l = max(i - locations[i], 0)
		r = min(i + (locations[i] + 1), n)
		dp[l] = max(dp[l], r)
    answer = 1
    r = dp[0]

    new = 0
    for i in range(n):
		new = max(new,dp[i])

		if (i == r):
			answer += 1
			r = new

    return answer

