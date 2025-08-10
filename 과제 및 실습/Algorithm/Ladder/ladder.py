'''
    사다리 게임을 통해 누가 아이스크림을 구입할 지 결정하기
    어느 사다리를 고르면 X 표시로 도착하게 되는지 궁금
    ex) 출발점 x = 0 및 x = 9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 추가되고
        이 막대들 사이에 가로 방향의 선들이 또한 랜덤하게 연결
    X 표시는 2로 표현함

    제약 조건
        - 한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우는 없다.

    입력
        - 첫 번째 줄 : 테스트 케이스의 번호
        - 두 번째 줄 : 테스트 케이스

    출력
        - #t 답
'''

import sys
sys.stdin = open('input.txt')

def ladder_game(idx, end_num):
    global ladder
    if idx == 0:
        return end_num

    if end_num > 0 and ladder[idx][end_num-1] == 1:
        while end_num > 0 and ladder[idx][end_num-1] == 1:
            end_num -= 1
        return ladder_game(idx-1, end_num)

    elif end_num < 99 and ladder[idx][end_num+1] == 1:
        while end_num < 99 and ladder[idx][end_num+1] == 1:
            end_num += 1
        return ladder_game(idx - 1, end_num)

    return ladder_game(idx-1, end_num)



for _ in range(10):
    tc = int(input())
    ladder = [[0]* 100 for _ in range(100)]
    for i in range(100):
        ladder[i] = list(map(int, input().split()))
    # print(ladder)
    for idx in range(100):
        if ladder[99][idx] == 2:
            end_num = idx
    print(f'#{tc} {ladder_game(99, end_num)}')