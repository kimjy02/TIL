'''
    다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.
        - 8개의 숫자를 입력받는다.
        - 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.
        - 다음 첫 번째 수는 2 감소한 뒤 맨 뒤로,
        - 그 다음 첫 번쨰 수를 3을 감소하고 맨 뒤로,
        - 그 다음 수는 4
        - 그 다음 수는 5를 감소한다.
        - 이와 같은 작업을 한 사이클이라 한다.
        - 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지하며, 프로그램은 종료
        - 이때 8자리의 숫자 값이 암호가 된다.

    제약 사항
        - 주어지는 각 수는 integer 범위를 넘지 않는다.
        - 마지막 암호 배열은 모두 한 자리 수로 구성되어 있다.

    입력
        - 총 10개의 테스트 케이스가 주어진다.
        - 첫 번째 줄 : 테스트 케이스 번호
        - 두 번째 줄 : 8개의 데이터

    출력
        - #{tc} {답}
'''
import sys
sys.stdin = open('input.txt')

from collections import deque

def cycle(list):
    while list[7] != 0:
        for i in range(1, 6):
            if list[0]-i > 0:
                list[0] -= i
                out = list.popleft()
                list.append(out)
            elif list[0]-i <= 0:
                list.popleft()
                list.append(0)
                break


for _ in range(10):
    tc = int(input())
    password = deque(map(int, input().split()))
    cycle(password)
    # answer = list(password)

    # print(f'#{tc} {answer[0]} {answer[1]} {answer[2]} {answer[3]} {answer[4]} {answer[5]} {answer[6]} {answer[7]}')
    print(f'#{tc} {" ".join(map(str, password))}')