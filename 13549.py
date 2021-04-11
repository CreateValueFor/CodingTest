#1차원
# 1초에 1만큼 이동 가능
#위치 x 일때 순간이동은 0초에 2*x만큼 이동 가능
#기회비용 연산 하기

import sys
sys.setrecursionlimit(10**6)

location = list(map(int,(sys.stdin.readline().strip().split())))

#트리형식으로 구현할 생각
# 짝수가 나오면 홀수가 나오거나 구하려는 수의 2배이하가 되기 전까지 s
#계속 나누기
#가장 간단한 풀이를 생각해 낼 필요가 있을 듯 함
class Node():
    def __init__(self,item,count):
        self.item = item
        self.right = None
        self.left = None
        self.count = count

class FindingTree(object):

    def __init__(self, N, K):
        self.N = N
        self.K = K
        self.K = self.K[0]
        # if self.N > self.K:
        #     self.N = self.K
        #     self.K = self.N
        self.root = Node(K,0)


    def teleport(self,node):

        while node.item % 2 == 0 and node.item >= self.N * 2:
            node.item = node.item //2

        return node

    def walk(self, node):
        node.right = self.teleport(Node(node.item+1,node.count))
        node.left = self.teleport(Node(node.item-1,node.count))
        node.right.count += 1
        node.left.count += 1

        return node.right, node.left

    def check(self, node):
        if node.item == self.N:
            return True
        else:
            return False

    def bigKconstruct(self,root):
        
        root = self.teleport(root)
        a, b = self.walk(root)
        if self.check(a) or self.check(b):
            print(a.count)
            sys.exit()
        while not (self.check(a) or self.check(b)):
            self.bigKconstruct(a)
            self.bigKconstruct(b)



        

tmp = FindingTree(location[0],[location[1]])
tmp.bigKconstruct(Node(tmp.K,0))

