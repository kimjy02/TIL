'''
    양수와 + - 괄호를 이용해 식을 생성
    그리고 괄호를 모두 지움
    이 식에 적절히 괄호를 넣어서 식의 값을 최소로 만들려고 함
    괄호를 적절히 넣어서 최소로 만드는 프로그램 작성

    [입력]
        괄호를 제외한 식
            - 첫번째와 마지막 문자는 숫자
            - 연속해서 두 개 이상의 연산자가 나타나지 않음
            - 5자리보다 많이 연속되는 숫자 X
            - 수는 0으로 시작할 수 있음
            - 입력으로 주어지는 식의 길이는 50 이하
'''
from collections import deque
expression = deque(map(str, input().strip()))

values = deque()

before_value = ''
while expression:
    current = expression.popleft()
    if current == '+' or current == '-':
        values.append(int(before_value))
        values.append(current)
        before_value = ''
    else:
        before_value += current

    if len(expression) == 0 and before_value != '':
        values.append(int(before_value))

# print(values)

# print(values.index('-'))
answer = []
calculate_value = 0
while values:
    value = values.popleft()
    if type(value) == int:
        calculate_value += value
    elif value == '+':
        pass
    else:
        answer.append(calculate_value)
        calculate_value = 0

    if len(values) == 0 and calculate_value != 0:
        answer.append(calculate_value)

# print(answer)
result = answer[0]
for a in range(1, len(answer)):
    result -= answer[a]

print(result)