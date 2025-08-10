'''
    테이블 위에 자성체들이 놓여 있다.
    자성체들은 성질에 따라 색이 부여되는데,
    푸른 자성체의 경우 N극에 이끌리는 성질을 가지고 있고,
    붉은 자성체의 경우 S극에 이끌리는 성질이 있다.

    아래와 같은 테이블에서 일정 간격을 두고 강한 자기장을 걸었을 때,
    시간이 흐른 뒤 자성체들이 서로 충돌하여 테이블 위에 남아있는 교착 상태 개수를 구하라.

    제약 사항
        - 자성체는 테이블 앞뒤 쪽에 있는 N극 또는 S극에만 반응하며
        - 자성체끼리는 전혀 반응하지 않는다.
        - 테이블의 크기 : 100 X 100

    입력
        - 10개의 테스트 케이스가 주어진다.
        - 첫 번째 줄 : 정사각형 테이블의 한 변의 길이 : 100
        - 두 번째 줄 : 100 X 100 테이블의 초기 모습
            - 1 : N극 성질을 가지는 자성체
            - 2 : S극 성질을 가지는 자성체
            - 테이블 윗부분은 N극, 아랫부분은 S극

    출력
        - #tc {교착 상태 개수}
'''
import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    total = 0
    # print(len(table))
    # print(table[0])
    for col in range(100):
        count = 0
        stack = []
        for row in range(100):
            if table[row][col] == 1:
                stack.append(table[row][col])
            if table[row][col] == 2:
                if len(stack) != 0:
                    stack = []
                    count += 1
        total += count
    print(f'#{tc} {total}')
