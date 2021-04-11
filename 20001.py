class Stack:
    # 리스트를 이용하여 스택 생성
    def __init__(self):
        self.top = []
    #스택의 크기를 출력
    def __len__(self):
        return len(self.top)
    #스택 내부 자료를 string 으로 변환하여 반환
    def __str__(self):
        return str(self.top[::1])
    
    def push (self, item):
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

tmp = input()
stack = Stack()
while True: #tmp != "고무오리 디버깅 끝":
    tmp = input()
    if tmp == "문제":
        stack.push(tmp)
    elif tmp == "고무오리":
        if stack.isEmpty():
            stack.push(tmp)
            stack.push(tmp)
        else:
            stack.pop()
    else: 
        break
if stack.isEmpty():
    print("고무오리야 사랑해")
else:
    print('힝구')
