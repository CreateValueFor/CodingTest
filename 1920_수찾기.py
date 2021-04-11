import sys

input = sys.stdin.readline

N = int(input())
n_list = list(map(int,input().split()))
M = int(input())
m_list = list(map(int,input().split()))

n_list.sort()

def binary_search(array, target, start, end):
    
    while start<= end:
        mid = (start+end)//2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return 0

for m in m_list:
    print(binary_search(n_list, m, 0, N-1))