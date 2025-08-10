'''
    사다리타기를 통해 아이스크림 구입할지 결정하기
    어느 사다리를 고르면 X 표시에 도착하게 되는지 확인
    100 X 100 크기의 2차원 배열로 주어진 사다리에 대해서
    지정된 도착점에 대응되는 출발점 X를 반환하는 코드를 작성하라.
    ((도착 지점은 2로 표현, 사다리는 1로 표현))

    제약 사항
        - 한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우 X

    입력
        - 첫번째 줄 : 테스트 케이스의 번호
        - 두번째 줄 : 테스트 케이스
        - 총 10개의 테스트 케이스가 주어짐

    출력
        - #tc 도착하게 되는 출발점의 x좌표
'''

# import sys

# sys.stdin = open('input.txt')

def ladder_game(idx, end_idx):    # 마지막 열부터 위로 올라가는 함수
    if idx == 0:     # 첫 번째 열에 도달했을 때, 행 번호 출력
        return end_idx

    # 행 번호가 99보다 작고 같은 열에서 행 번호 + 1의 값이 1인 경우,
    # 행 번호 + 1이 1일 때까지 행 번호(end_idx) + 1
    # 행 번호 + 1이 1이 아니면 재귀함수를 이용해서 열 번호 -1 실행
    if end_idx < 99 and ladder[idx][end_idx+1] == 1:
        while end_idx < 99 and ladder[idx][end_idx+1] == 1:
            end_idx += 1
        return ladder_game(idx-1, end_idx)

    # 행 번호가 0보다 크고 같은 열에서 행 번호 - 1의 값이 1인 경우,
    # 행 번호 - 1이 1일 때까지 행 번호(end_idx) - 1
    # 행 번호 - 1이 1이 아니면 재귀함수를 이용해서 열 번호 -1 실행
    elif end_idx > 0 and ladder[idx][end_idx-1] == 1:
        while end_idx > 0 and ladder[idx][end_idx-1] == 1:
            end_idx -= 1
        return ladder_game(idx-1, end_idx)

    # 행 번호 기준 양 옆이 모두 0 값이라면, 열 번호 - 1인 재귀함수 실행
    else:
        return ladder_game(idx-1, end_idx)

for _ in range(10):
    tc = int(input())  # 테스트 케이스 번호
    ladder = [[0]*100 for i in range(100)]

    for i in range(100):
        ladder[i] = list(map(int, input().split()))

    for j in range(len(ladder[99])):
        if ladder[99][j] == 2:
            end_idx = j

    print(f'#{tc} {ladder_game(99, end_idx)}')