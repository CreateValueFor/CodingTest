#트리의 성질, 정점이 n개 간선이 n-1개 있다.
#임의의 두 정점에 대해서 경로가 유일하다. 
#모두 연결되어있지만 순환해선 안된다. 
#함수 지역변수 글로벌 변수 제대로 공부 다시할 것
#함수 안에서 리스트같은 경우 global 사용 안해도된다.


import sys

input = sys.stdin.readline


count = 1
def dfs( current, nextn):
    global is_cycle

    
    for i in range(1,N+1):
        print(tree[nextn][current] == 1 )
        
        if tree[nextn][current] == 1 and i != nextn:

            if not(visited[i]):
                dfs(nextn, i)  
            else:     
                is_cycle = True
                continue
    return is_cycle

        

while True:
    is_cycle = False
    N, M = map(int, input().split())
    #while문을 써서 0,0이아닐 땐 항상 작동하도록
    if N ==0 and M ==0:
        break
    #N+1짜리 배열과 행렬 생성
    visited = [0 for i in range(N+1)]
    tree = [[0 for i in range(N+1)] for j in range(N+1)]
    answer = 0
    for i in range(M):

        n1, n2 = map(int,input().split())
        tree[n1][n2] = 1
        tree[n2][n1] = 1


    for i in range(1, N+1):
        if not(visited[i]):
            is_cycle = False
            is_cycle = dfs( 0,i)
            if not(is_cycle):
                answer+= 1


    result = ""
    if (answer == 1):
        result += 'Case ' + str(count) + ": There is one tree"
    elif(answer == 0):
        result += 'Case ' + str(count) + ": No trees."
    else:
        result += 'Case ' + str(count)+ ": A forest of "+str(answer)+ " trees."
    print(result)
    count += 1
