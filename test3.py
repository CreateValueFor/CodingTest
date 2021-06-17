import heapq
INF = 1e9

def solution(n, costs):
    answer = 0
    graph = [[] for i in range(n)]
    distance = [INF] * n
    visited = [False] * n
    
    for cost in costs:
        a, b, c = cost
        graph[a].append((b,c))
        graph[b].append((a,c))
    for i in range(n):
        if visited[i] == False:
            minV = INF
            for info in graph:
                if info[1] < minV:
                    minV = info[1]
            answer += minV
    
    
    return answer
print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))