user1 = [1,2,3,4,5]
user2 = [2,1,2,3,2,4,2,5]
user3 = [3,3,1,1,2,2,4,4,5,5]

def grading(user, answers):
    count = 0
    tmp = len(user)
    for i in range(len(answers)):
        num = i%tmp
        if answers[i] == user[num]:        
            count += 1
    print(user, count)
    return count

def solution(answers):
    answer = []
    user1_count = grading(user1, answers)
    user2_count = grading(user2, answers)
    user3_count = grading(user3, answers)
    if user1_count == user2_count and user1_count == user3_count :
        return[1,2,3]
    if user1_count > user2_count and user1_count > user2_count:
        return [1]
    if user2_count > user1_count and user2_count > user3_count:
        return [2]
    if user3_count > user2_count and user3_count > user1_count:
        return [3]
    if user1_count == user2_count and user1_count > user3_count:
        return [1,2]
    if user1_count == user3_count and user1_count > user2_count:
        return [1,3]
    if user3_count == user2_count and user2_count > user1_count:
        return [2,3]
    

print(solution())