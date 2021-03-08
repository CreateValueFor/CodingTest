import itertools

# pool = ['A', 'B','C']

# for i in range(1,len(pool)+1):
#     print(list(itertools.permutations(pool,i)))

def solution(numbers):
    count = 0
    per_save = []
    for i in range(1,len(numbers)+1):
        perm = list(itertools.permutations(numbers,i))
        for j in perm:
            tmp = ''
            if j[0] != '0': 
                for tup in j:
                    tmp += tup
            if tmp == '1' or tmp == '':
                continue
            if tmp in per_save:
                continue
            per_save.append(tmp)

            isdecimal = True
            for k in range(2,int(tmp)):
                if int(tmp) % k == 0:
                    isdecimal = False
            if isdecimal == True:
                # print(tmp)
                count += 1
    return count

print(solution('17'))
# print(solution('011'))
# print(solution('17'))