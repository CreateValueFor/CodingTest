import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input())for _ in range(N)]
numbers.sort()
M = int(input())
require = [int(input()) for _ in range(M)]

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) //2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            start = mid+1
        else:
            end = mid-1
        
    return False

for num in require:
    print(binary_search(numbers, num, 0, N-1))
