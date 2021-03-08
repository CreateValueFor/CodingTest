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
            print("Underflow")
            exit()
    
    def isEmpty(self):
        return len(self.top) == 0
    
    def size(self):
        return len(self.top)

num = input()

for i in range(1,int(num)+1):
    test = input()
    words_list = test.split()
    tmp = Stack()
    for words in words_list:
        tmp.push(words)
        # print(tmp.pop())
    temp = ""
    for words in words_list:
        temp += tmp.pop() +" "
        # print(tmp.pop())
    print("Case #{}: {}".format(i, temp))