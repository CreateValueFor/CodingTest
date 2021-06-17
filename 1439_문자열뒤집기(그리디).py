data = input()
tmp = 0
answer = 0
for i in range(1,len(data)):
  if data[i] != data[i-1]:
    tmp+= 1
if tmp % 2 == 1:
  answer = tmp //2 + 1
else: 
  answer = tmp //2


print(answer)