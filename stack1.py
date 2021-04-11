class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return not self.items

stk = stack()        # stack 객체 생성
print(stk)           # stack object 생성 확인
print(stk.isEmpty()) # 처음에는 아무것도 들어있지 않으므로 True 출력
stk.push(1)          # stk 에 1을 넣음
stk.push(2)          # stk 에 2를 넣음
print(stk.pop())     # stk 에 2가 꺼내지면서 출력 됨
print(stk.pop())     # stk 에 1가 꺼내지면서 출력 됨
print(stk.isEmpty())

