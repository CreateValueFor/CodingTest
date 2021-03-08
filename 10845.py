import sys
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data 
class SLL:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        else:
            self.head = node

    def deleteAtFirst(self):
        if self.head:
            cur = self.head.data 
            self.head = self.head.next
            return cur
        else:
            return -1

    def size(self):
        cur_i = 0
        curn = self.head
        while curn:
            cur_i += 1
            curn = curn.next
        return cur_i
    
    def back(self):
        curn = self.head
        while curn.next:
            curn = curn.next
        return curn.data
class Queue:

    def __init__(self):
        self.box = SLL()

    def push(self, item):
        self.box.append(Node(int(item)))
    
    def pop(self):
        return self.box.deleteAtFirst()

    def size(self):
        return self.box.size()

    def empty(self):
        if self.box.head:
            return 0
        else:
            return 1

    def front(self):
        return self.box.head.data 
    
    def back(self):
        if self.empty():
            return -1
        else:
            return self.box.back()

num = input()
que = Queue()
for _ in range(int(num)):
    tmp = sys.stdin.readline().strip().split()
    if len(tmp) >1:
        que.push(tmp[1])
    else:
        if tmp[0] == 'front':
            print(que.front())
        elif tmp[0] == 'size':
            print(que.size())
        elif tmp[0] == 'pop':
            print(que.pop())
        elif tmp[0] == 'empty':
            print(que.empty())
        elif tmp[0] == 'back':
            print(que.back())