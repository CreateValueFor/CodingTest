import sys 
input = sys.stdin.readline
# x, y ,age, is dead
N, M, K = map(int,input().split())
tree_list = [[[] for i in range(N)]for i in range(N)]
food_list = [list(map(int,input().split()))for i in range(N)]
# graph = [list(map(int,input().split()))for i in range(N)]



for i in range(M):
    x, y, age = map(int, input().split())
    tree_list[x-1][y-1].append(age)


nourishment = [[5 for i in range(N)]for i in range(N)]
#나이기준으로 sort 한 후 사용
def spring():

    # print(tree_list)
    for i in range(N):
        for j in range(N):
            if len(tree_list[i][j])>0:
                # print(tree_list[i][j])
                tree_list[i][j].sort()
                temp_tree,dead_tree = [],0
                for age in tree_list[i][j]:
                    if nourishment[i][j] < age:
                        dead_tree += age //2
                    else:
                        nourishment[i][j] -= age
                        age += 1
                        temp_tree.append(age)
                nourishment[i][j] += dead_tree
                tree_list[i][j] = []
                tree_list[i][j].extend(temp_tree)              


def fall():
    dx = [-1,-1,-1,0,0,+1,+1,+1]
    dy = [-1,0,+1,-1,+1,-1,0,+1]
    for i in range(N):
        for j in range(N):
            for age in tree_list[i][j]:
                # print(type(tree_list[i][j][tree]))
                if age % 5 == 0:
                    for k in range(8):
                        nx = i + dx[k]
                        ny = i + dy[k]
                        if 0<= nx < N and 0<= ny < N:
                            tree_list[nx][ny].append(1)

def winter():
    for i in range(N):
        for j in range(N):
            nourishment[i][j] += food_list[i][j]

for i in range(K):
    spring()
    # summer()
    fall()
    winter()
            
answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree_list[i][j])
print(answer)


