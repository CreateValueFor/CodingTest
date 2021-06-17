data = list(map(int,list(input())))
answer = data[0]
for i in data[1:]:
  if i <= 1 or answer <= 1:
    answer += i
    continue
  answer *= i
print(answer)
