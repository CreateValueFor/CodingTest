# 간선이 1개만 있는 노드가 3개 이상 연결되어 있는 노드는 무조건 병원을 세운다
# 간선이 1개인 노드엔 병원을 세우지 않는다.
# 병원이 인접한 노드는 배제시킨다
# 1, 2, 3 를 반복한다.

import copy
def hospital(city_nodes, city_from, city_to):
    graph = [[] for _ in range((city_nodes+1))]
    edges = [0] * (city_nodes+1)
    visited = [False] * (city_nodes+1)
    visited_counted = [False] * (city_nodes+1)
    answer = 0

    for i in range(len(city_from)):
        a, b = city_from[i], city_to[i]
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, city_nodes+1):
        edges[i] = len(graph[i])
    
    for i in range(1, city_nodes+1):
        if edges[i] == 1:
            visited[graph[i][0]] = True
    visited_counted = visited[:]
    answer += visited.count(True)

    #인접한 병원이 있는 노드는 전부 True로 변경
    for i in range(1, city_nodes+1):
        if visited[i] == True:
            for node in graph[i]:
                visited_counted[node] = True
    visited = visited_counted[:]

    while visited.count(False) != 1:
        graph_tmp = [[] for _ in range((city_nodes+1))]
        edges_tmp = [0] * (city_nodes+1)
        # 인접한 병원이 없는 노드들 중 edge 갯수 구하기
        for i in range(1, city_nodes+1):
            if visited[i] == False:
                tmp = 0
                if len(graph[i])== 0:
                    visited[i] = True
                    continue
                for node in graph[i]:
                    if visited[node] == False:
                        tmp += 1
                        graph_tmp[i].append(node)
                edges_tmp[i] = tmp

        # 연결이 1개인 노드들에 대해 다시 위의 과정 반복
        for i in range(1, city_nodes+1):
            if edges_tmp[i] ==1 and visited[i] == False:
                visited[graph_tmp[i][0]] = True

        answer += visited.count(True) - visited_counted.count(True)
        visited_counted = visited[:]
        for i in range(1, city_nodes+1):
            if visited[i] == True:
                for node in graph_tmp[i]:
                    visited_counted[node] = True
        visited = visited_counted[:]
        graph = copy.deepcopy(graph_tmp)
        edges = copy.deepcopy(edges_tmp)


    return answer


city_nodes = 12
city_from = [1,1,6,1,1,2,11,12,4,12,6]
city_to = [11,2,7,6,12,3,10,9,5,8,4]

city_nodes_test = 11
city_from_test = [7, 2, 7, 3, 1, 11, 2, 3, 8, 10]
city_to_test = [5, 9, 1, 9, 8, 6, 6, 10, 11, 4]
print(hospital(city_nodes,city_from,city_to))
print(hospital(city_nodes_test,city_from_test,city_to_test))