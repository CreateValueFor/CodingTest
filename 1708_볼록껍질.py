import sys
input = sys.stdin.readline
point_num = int(input())
point_list = []

def ccw(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    t = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    return t<=0

for i in range(point_num):

    x, y = (map(int,input().split()))
    point_list.append([x,y])


point_list.sort(key=lambda a : a[0])
point_list.sort(key=lambda a : a[1])

start_x = point_list[0][0]
start_y = point_list[0][1]
d_list = [[-987654321,0,start_x, start_y]]
for i in range(1,point_num):
    y =  point_list[i][1]
    x = point_list[i][0]
    dy = y - start_y
    dx = x - start_x
    dist = (dy**2 + dx**2)**(1/2)
    if dx == 0:
        d_list.append([987654321,dist,x,y])
        continue
    d_list.append([dy/dx,dist,x,y])
d_list.sort(key = lambda a : a[0])
d_list.sort(key = lambda a : a[1])
# pop해줘야함
stack = []
stack.append(point_list[0])
for i in range(point_num):
    point = d_list[i][2:]
    while len(stack) > 1 and (ccw(stack[-2],stack[-1],point)):
        stack.pop()
    stack.append(point)


print(len(stack))

