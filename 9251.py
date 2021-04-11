import sys 
#strip 함수는 문자열의 양 끝에 존재하는 공백과 \n을 제거해주는 것
#upper 함수는 문자열을 대문자로 만들어 주는 것
string1 = sys.stdin.readline().strip()
string2 = sys.stdin.readline().strip()

len1 = len(string1) 
len2 = len(string2)
#행렬 생성
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)] 
# print(matrix)
for i in range(1, len1 + 1): 
    for j in range(1, len2 + 1): 
        if string1[i - 1] == string2[j - 1]: 
            matrix[i][j] = matrix[i - 1][j - 1] + 1 
        else: 
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1]) 
print(matrix[-1][-1])

