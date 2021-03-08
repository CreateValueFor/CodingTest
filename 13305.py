#N개의 도시, 일직선, 왼쪽에서 오른쪽, 도시 사이 도로들 길이 다를 수 있음

#처음 출발시 주유소, 기름 통 크기 무제한, 원 안 숫자는 도시의 주유소
#리터당 가격
#주유소 기름가격, 도로길이 인풋
#그리디 알고리즘은 탐욕 알고리즘 또는 욕심쟁이 알고리즘이라고도 불리는데요. 미래를 생각하지 않고 각 단계에서 가장 최선의 선택을 하는 기법입니다.
import sys

input = sys.stdin.readline

num = int(input())
road_length_list = list(map(int, input().strip().split()))
fee_list = list(map(int, input().strip().split()))

minfee = sys.maxsize
result = 0

for i in range(num-1):
    if i ==0 :
        minfee = fee_list[0]
    else:
        minfee = min(minfee, fee_list[i])
    result += road_length_list[i] * minfee

print(result)

