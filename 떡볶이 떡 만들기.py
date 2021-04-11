import sys
input = sys.stdin.readline

N, M = map(int,input().split())
riceCake= list(map(int,input().split()))

def slice(height):
    sum_length = 0
    for rice in riceCake:
        if rice > height:
            sum_length += rice-height
    return sum_length

def binary_search(array, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end)//2
        sum_length = slice(mid)
        if sum_length < target:
            end = mid-1
        else:
            result = mid
            start = mid+1
    return result


firstheight = max(riceCake)
print(binary_search(riceCake, M, 0, firstheight))