'''
   문자열로 이루어진 계산식이 주어질 때, 이 계산식응ㄹ 후위 표기식으로 바꾸어 계산하는 프로그램 작성
   ex)
    "3+4+5+6+7"이라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.
    => "34+5+6+7+"
    변환된 식을 계산하면 25를 얻을 수 있다.
    문자열 계산식을 구성하는 연산자는 + 하나뿐이며 피연산자인 숫자는 0~9의 정수만 주어진다.

    입력
        - 첫번째 줄 : 문자열 계산식의 길이
        - 두번째 줄 : 문자열 계산식
        - 총 10개의 테스트 케이스가 주어진다.

    출력
        - #[idx] ans
'''

import sys
from collections import deque

sys.stdin = open('input.txt')

def calculator(idx, list):
    global total

    if len(list) == 0:
        return total

    if idx == 0:
        total = list[idx]
        list.popleft()

    if list[0] == plus:
        total += list[1]
        list.popleft()
        list.popleft()
    # print(total)
    return (calculator(idx+1, list))

plus = '+'

for tc in range(1, 11):
    N = int(input())     # 문자열 계산식의 길이
    string = deque(map(str, input().strip()))
    total = 0
    for i in range(0, len(string), 2):
        string[i] = int(string[i])

    # total = calculator(0, string)
    print(f'#{tc} {total}')
