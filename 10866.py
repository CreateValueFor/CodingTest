#doubly linked list 를 이용한 덱 구현 
import sys

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList(object):

    def __init__ (self):
        self.head = None
        self.tail = None
        
    def appendFirst(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node
    
    def appendTail(self, node):
        if self.head:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        else: 
            self.head = node
            self.tail = node

    def seekFirst(self):
        return self.head.data
    def seekTail(self):
        return self.tail.data

    def deleteFirst(self):
        if self.head:
            cur = self.head.data
            curn = self.head
            self.head.next = None
            self.head = curn.next
            # self.head.prev = None
            return cur
        else: return -1
    def deleteTail(self):
        if self.tail:
            cur = self.tail.data
            self.tail.prev = None
            self.tail = self.tail.prev
            # self.tail.next = None
            return cur
        else:
            return -1

    def size(self):
        curn = self.head
        n = 0
        while curn :
            curn = curn.next
            n += 1
        return n
    
    def empty(self):
        if self.size() == 0:
            return 1
        else: return 0
input = sys.stdin.readline
dll = doublyLinkedList()
if __name__ == '__main__':
    num = input()
    for _ in range(int(num)):
        tmp = input().strip().split()
        if tmp[0] =="push_front":
            node = Node(tmp[1])
            dll.appendFirst(node)
        elif tmp[0] == "push_back":
            node = Node(tmp[1])
            dll.appendTail(node)
        elif tmp[0] == "pop_front":
            print(dll.deleteFirst())
        elif tmp[0] == "pop_back":
            print(dll.deleteTail())
        elif tmp[0] == "size":
            print(dll.size())
        elif tmp[0] == 'empty':
            print(dll.empty())
        elif tmp[0] == 'front':
            print(dll.seekFirst())
        else:
            print(dll.seekTail())
