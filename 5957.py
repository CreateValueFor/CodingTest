 #스택 클래스
class Stack:
    def __init__(self):
        self.top = []
    def __len__(self):
        return len(self.top)
    
    def push(self,item):
        self.top.append(item)
    
    def pop(self):
        #if Stack is not empty
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print("Stack underflow")
            exit()
    
    def clear(self):
        self.top = []
    #자료가 포함되어 있는지 여부 반환
    def isContain(self, item):
        return item in self.top
    
    #스택에서 top의 값을 읽어온다.
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            # print("Underflow")
            # exit()
            return -1
    
    def isEmpty(self):
        return len(self.top) == 0
    
    def size(self):
        return len(self.top)

 #3개의 스택이 필요할 것 

dirty_dish = Stack()
washed_dish = Stack()
cleaned_dish = Stack()

#몇개의 접시를 세탁하는가
num_dish = input()
for  dish in range(1, int(num_dish) + 1):

    dirty_dish.push(int(num_dish) + 1 - dish)

n = 0
while n != int(num_dish):

    tmp = input().split()

    #첫번 째 수가 1이면 베시가 세탁
    if tmp[0] == '1':
        for j in range(int(tmp[1])):
            dish = dirty_dish.pop()
            washed_dish.push(dish)
    #첫 번째 수가 2이면 칸무가 닦기
    else:
        for k in range(int(tmp[1])):
            dish = washed_dish.pop()
            cleaned_dish.push(dish)
        n += int(tmp[1])

for sequence in range(int(num_dish)):
    print(cleaned_dish.pop())


