import sys

class Stack:

    def __init__(self):
        self.box = []

    def __len__(self):
        return(len(self.box))
    
    def push(self, item):
        self.box.append(int(item))


    def pop(self):
        if self.empty():
            return -1
        else:            
            return self.box.pop(-1)

    def size(self):
        return len(self.box)

    def empty(self):
        if len(self.box) == 0:
            return 1
        else:    
            return 0 
    
    def top(self):
        if self.empty():
            return -1
        else:
            return self.box[-1]

num = input()

stack =Stack()

for _ in range(int(num)):
    tmp = sys.stdin.readline().split()
    if len(tmp) >1:
        stack.push(tmp[1])
    else:
        if tmp[0] == 'top':
            print(stack.top())
        elif tmp[0] == 'size':
            print(stack.size())
        elif tmp[0] == 'pop':
            print(stack.pop())
        elif tmp[0] == 'empty':
            print(stack.empty())