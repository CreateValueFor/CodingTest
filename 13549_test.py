N, K = map(int, input().split())

path = [(N, 0)]
visited = [False for _ in range(100001)]
answer = float('inf')
while path:
    location, time = path.pop(0)
    visited[location] = True
    if location == K:
        answer = min(answer, time)
    if location * 2 <= 100000 and not visited[location * 2]:
        path.append((location * 2, time))
    if location + 1 <= 100000 and not visited[location + 1]:
        path.append((location + 1, time + 1))
    if 0 <= location - 1 <= 100000 and not visited[location - 1]:
        path.append((location - 1, time + 1))
print(answer)