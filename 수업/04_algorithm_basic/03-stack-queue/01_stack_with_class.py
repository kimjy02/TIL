class Stack:
    # 생성자 함수
    def __init__(self, capacity = 10):
        self.capacity = capacity            # 이 자료구조의 최대 수용 가능 공간
        self.items = [None] * capacity      # 내 최대 크기 만큼 None으로 채운다.
        self.top = -1
        # 왜 top이 0이 아닌 -1로 초기화 하느냐?
        # 여기서 -1은 리스트의 마지막을 의미하는 게 아니라,
        # push 연산을 진행할 때, top의 값을 1 증가시키고, 그곳에 값을 삽입


    # 주어진 값을 삽입
    def push(self, item):
        # 예외 처리 -> is_full 하다면, ... 어떠한 치릴
        if self.is_full() :               # True라면 값을 삽입할 수 없음
            print('Stack is Full!!!')
            return
            # raise IndexError('Stack is Full')
        self.top += 1                   # 올바른 삽입 위치 찾기
        self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            print('Stack is Empty!!!')
            return
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item    # 제거한 값을 반환
        # stack이 가득 찼음을 어떻게 알 수 있을까?

    def is_full(self):
        return self.capacity -1 == self.top

    def is_empty(self):
        return self.top == -1




# stack 자료구조 인스턴스 생성 시, 이 자료구조의 최대 크기도 함께 넘겨줘야 한다.
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())
# print(stack.peek())
print(stack.is_empty())
print(stack.pop())
print(stack.pop())
