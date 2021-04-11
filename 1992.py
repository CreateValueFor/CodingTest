import sys

n = int(input())
table=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]#x행 y열

count_list = [0 for i in range(n)]
def quadtree(x,y,n):
    if(n==1):
        return str(table[x][y])
    check = table[x][y]
    
    result = []
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != table[i][j]:
                #차원 들어가면 그 차원 안에서 해결해주느 ㄴ것이 좋다.
                result.append('(')
                result.extend(quadtree(x,y,n//2))
                result.extend(quadtree(x+n//2,y,n//2))
                result.extend(quadtree(x+n//2,y+n//2,n//2))
                result.extend(quadtree(x,y+n//2,n//2))
                result.append(')')
                return result
    
    return str(table[x][y])

print(''.join(quadtree(0,0,n)))
