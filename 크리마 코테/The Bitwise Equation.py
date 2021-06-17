# def bitwiseEquations(a, b):
#     answer = [0] * len(a)
#     for i in range(len(a)):
#         for j in range(a[i]):
#             x = j
#             y = a[i] - j
#             if x ^ y == b[i]:
#                 answer[i] = (2*x + 3*y)
#                 break
#         print(x,y)
#     return answer
def test(a, b):
    n = len(a)
    answer = [0] * n
    
    for i in range(n):
        if a[i] < b[i]:
            continue
        Flag = True
        bi_a = format(a[i],'b')
        bi_b = format(b[i],'b')
        tmp = len(bi_a) - len(bi_b)
        bi_b = ('0'* tmp) + bi_b
        comp = '0' * len(bi_a)
        for j in range(len(bi_b)-1,0,-1):

            if bi_a[j] != bi_b[j] :
                #숫자가 다를 때 bi_a[i]가 0인 경우        
                if bi_a[j] =='0' and (j+1)<len(bi_a):
                    if (j-1) >=0:
                        if bi_a[j-1:j+2] == "100" and bi_b[j-1:j+2] =="010":
                            comp = comp[:j+1] + '1' + comp[j+2:]
                            bi_a = bi_a[:j] + '0' + bi_a[j+1:]
                        else: 
                            Flag = False
                            break
                elif bi_a[j] =='1' and (j+1)<len(bi_a):
                    if bi_a[j:j+2] =='10' and bi_b[j:j+2] == '00':
                        comp = comp[:j+1] + '1' + comp[j+2:]
                        bi_a = bi_a[:j] + '0' + bi_a[j+1:]

        x = int('0b{}'.format(comp),2)
        y = a[i] - x
        ans = 2* x + 3 * y
        if Flag == True:
            answer[i] = ans
    return answer



    

a = [29,36,57]
b = [25,18,3]
a1 = [15,139]
b1 = [15, 75]
a2 = [97,98,99,52]
b2 = [65,66,67,24]

# print(bitwiseEquations(a, b))
# bitwiseEquations(a1,b1)
# print()
# bitwiseEquations(a2,b2)
# print()
# bitwiseEquations([52],[24])

print(test(a,b))