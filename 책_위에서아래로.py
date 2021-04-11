import sys

input = sys.stdin.readline
N = int(input())
numbers = [int(input()) for _ in range(N)]

numbers = sorted(numbers, reverse=True)
