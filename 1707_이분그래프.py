import sys
from collections import deque

input = sys.stdin.readline
test_case = int(input())



def bfs(x):
    #탐색되지 않은 노드의 그룹을 1로 변경
    name[x] = 1
    q = deque()
    q.append(x)
    while q:
        a = q.popleft()
        #a와 인접한 모든 노드들에 대하여
        for i in graph[a]:
            #탐색되지 않은경우
            if name[i] == 0:
                #다른 색으로 칠해준 후 큐에 추가
                name[i] = -name[a]
                q.append(i)
            #탐색된 노드일 경우
            else:
                #색이 같다면 이분그래프가 아니다.
                if name[i] == name[a]:
                    return False
    return True

for i in range(test_case):
    #v, e 는 노드와 간선을 의미
    v, e= map(int,input().split())
    #이분그래프인가 아닌가를 나타내주는 불 값
    isTrue = True
    #인접리스트로 그래프 정보를 담기위해 graph 생성
    graph = [[]for i in range(v + 1)]
    #같은 그래프에 속하는지의 정보를 담은 리스트
    name = [0 for i in range(v + 1)]
    #모든 간선에 대하여 인접리스트로 정보저장
    for j in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    #모든 정점에 대하여 BFS알고리즘 진행
    for k in range(1, v+1):
        #아직 탐색되지 않은 경우 
        if name[k] == 0:
            if not bfs(k):
                isTrue = False
                break
    print("YES"if isTrue else "NO")