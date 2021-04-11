#2자리수 끼리면 둘끼리 비교해도 됨
#3자리수 끼리면 둘끼리 비교해도 됨
def solution(numbers):
    answer = ''
    s1= []
    s2small = []
    s2big = []
    s3smallbig = []
    s3smallsmall = []
    s3bigbig = []
    s3bigsmall = []
    s4 = []

    for num in numbers:
        if num>999:
            s4.append(num)
        if num>99:
            if str(num)[0]<str(num)[1]:
                if str(num)[0]<str(num)[2]:
                    s3bigbig.append(num)
                else:
                    s3bigsmall.append(num)
            else:

        elif num>9: 
            s2.append(num)
        else:
            s1.append(num)

    numbers = list(map(str, numbers))
    numbers.sort(key = lambda a : a[0],reverse=True )
    for num in numbers:
        answer += num
    return answer
print(solution([30,34,3,5,9]))