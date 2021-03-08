from collections import deque
def taxiDriver(pickup, drop, tip):
    # Write your code here
    answer = 0
    tup_list = []
    for i in range(len(pickup)):
        cost = drop[i] - pickup[i] + tip[i]
        tup_list.append((pickup[i],drop[i],tip[i],cost))
    
    tup_list.sort(key = lambda a : a[3],reverse = True)
    print(tup_list)
    tup_list.sort(key = lambda a: a[1])
    print(tup_list)
    start, end = 0,0
    for i in tup_list:
        if end <= i[0]:
            start = i[0]
            end = i[1]
            print(i)
            answer += i[3]
            
        
    return answer
    
pickup = [0,4,5]
drop = [3,5,7]
tip  = [1,2,2]

print(taxiDriver(pickup, drop, tip))
que = deque([0,1,2,3])
print(len(deque()))