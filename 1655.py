#정수를 외칠 때마다 중간값 외치기 홀수 // + 1
#외친 개수가 짝수라면 중간에 있는 두 수 중 작은 값, 짝수 //
#배열 인덱스에서 중위값을 이용해 찾기 
import heapq
import sys

input = sys.stdin.readline


#몇개의 수를 호출할 것인가
#기존의 자료구조를 어떻게 활용할 것인가가 먼저가 되어야 함
#중요한 것을 찾아서, 살려야 할 것, 살리지 않아도 될 것을 구분
#중복된 값을 어떻게 처리할 것인가
num = int(input())
left, right = [], []


for _ in range(num):
    insert_num = int(input())
    # que.enqueue(insert_num,insert_num)
    # tmp = que.count%2
    if len(left) == len(right):
        # print(que.queue[que.count//2 - 1][1])
        heapq.heappush(left,(-insert_num,insert_num))
    else:
        heapq.heappush(right,(insert_num,insert_num))
        # print(que.queue[que.count//2 ][1])
    if right and left[0][1] > right[0][1]:
        left_num = heapq.heappop(left)[1]
        right_num = heapq.heappop(right)[1]
        heapq.heappush(right,(left_num, left_num))
        heapq.heappush(left,(-right_num, right_num))
    print(left[0][1])




