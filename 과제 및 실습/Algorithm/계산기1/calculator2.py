# 문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램 작성

# ex: "3+4+5+6+7"라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.
# "34+5+6+7+" 변환된 식을 계산하면 25를 얻을 수 있다.

class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    def push(self, item):
        if self.is_full():
            raise IndexError("Stack is full")
        self.top += 1
        self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.items[self.top]

    def get_size(self):
        return self.top + 1




