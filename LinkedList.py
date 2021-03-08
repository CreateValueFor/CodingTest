class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


#Singly Linked list 클래스 선언
class SinglyLinkedList(object):

    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    