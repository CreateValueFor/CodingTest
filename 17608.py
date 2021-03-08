import sys

class Stack:
    def __init__ (self):
        self.top = []
    
    def push(self, item):
        self.top.append(item)
    
    def pop(self):
        return self.top.pop(-1)
        
    
num = input()
n = 0
height = 0
stack =Stack()
for _ in range(int(num)):
    stack.push(int(sys.stdin.readline().strip()))

for _ in range(int(num)):
    tmp = stack.pop()
    if height < tmp:
        n += 1
        height = tmp
    # print(type(stack.pop()))
print(n)