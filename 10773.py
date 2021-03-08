import sys 

class Stack():
    def __init__ (self):
        self.top = []
    def __len__ (self):
        return len(self.top)
    def push(self, item):
        self.top.append(item)
    def pop(self):
        return self.top.pop(-1)

#왜 스택이 더 유용할까?

input = sys.stdin.readline

a = Stack()
num = input()

for _ in range(int(num)):
    tmp = int(input())
    if tmp == 0 :
        a.pop()
    else:
        a.push(tmp)
sum = 0
for i in range(len(a)):
    sum += a.pop()

print(sum)