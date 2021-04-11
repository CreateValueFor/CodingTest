import sys

input = sys.stdin.readline

N = int(input())
n_list = list(map(int,input().split()))
M = int(input())
m_list = list(map(int,input().split()))

n_list.sort()

def binary_search_front(array, target, start, end):
    while start < end:
        mid = (start+end)//2
        if array[mid] >= target :
            end = mid
        else:
            start = mid+1
    return end

def binary_search_back(array, target, start, end):
    if array[N-1] == target:
        return N
    while start < end:
        mid = (start+end)//2
        if array[mid] > target :
            end = mid
        else:
            start = mid+1
    return end

for m in m_list:
    back = binary_search_back(n_list, m, 0, N-1)
    front = binary_search_front(n_list,m, 0, N-1)
    if front == 0 and n_list[back-1] != m:
        print(0, end=' ')
    else:
        print(back-front, end=' ')