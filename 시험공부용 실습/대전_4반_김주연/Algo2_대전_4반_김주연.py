'''
     세균들이 종류에 따라 서로 다른 속도로 증식한다는 사실을 알게 됨
     이 특징을 활용하면 세균 증식 과정으로 그림을 그릴 수 있을 것

     특징
        1. 각 세균은 시작 지점에서 최대로 퍼져 나갈 수 있는 크기가 정해져 있음
        2. 본인 자리에서 인접한 상하좌우 방향으로만 증식 가능
        3. 증식하려는 방향에 이미 다른 세균이 자리 잡고 있으면 더 이상 증식 불가
        4. 세균을 배양하는 배지를 벗어날 수 없음
        5. A부터 Z까지 세균이 있을 때, 알파벳은 동일 시간에 먼저 활성화되는 순서를 의미
        6. 세균의 종류는 항상 A부터 시작하며, 건너뛰는 경우 없이 순서대로 사용

    [제약사항]
        ex) 각 세균별 최대 증식가능 크기가 다음과 같을 때,
            - 세균 A : 2
            - 세균 B : 2
            - 세균 C : 2
            - 세균 D : 2

            각 세균의 최대 증식 크기는 동일하지만
            매 시간 가장 먼저 증식하는 세균은 A가 우선 증식되고, B, C, D 순서로 증식한다.
            
    [입력]
        1. T : 테스트 케이스 수
        2. N : 배지의 가로크기 / M : 배지의 세로크기 (5 <= N, M <= 100)
        3. K : 세균 종류 (1 <= K <= 26)
            - 세균 종류는 알파벳 순서에 따라 주어짐.
        4. A_i : 세균별 최대 증식 가능 크기 (1 <= A_i <= 100)
        5. N개씩 M번 줄에 걸쳐 세균 최초 배지 정보 제공
            - `.`은 비어있는 공간
    
    [출력]
    - #{tc} {배지 데이터}
    - 배지 데이터 출력 시 각 칸 사이에 공백이 있음에 유의
'''
import sys
sys.stdin = open('algo2_sample_in.txt')

# 상하좌우 방향
#     상  하  좌  우
dx = [+0, +0, -1, +1]
dy = [-1, +1, +0, +0]

def lab(info, kinds, size):
    # 증식 과정에서 info 값을 바꿨을 때, 방금 증식된 부분에서 다시 증식되는 것을 방지하기 위한 visited 생성
    visited = [[-1] * N for _ in range(M)]
    # 증식 크기가 가장 큰 경우를 기준으로 반복문 생성
    for c in range(max(size)):
        for kind in kinds:
            # c가 0부터 시작하기 때문에 c+1보다 크거나 같은 경우에만 반복문 실행
            if size[kind-1] >= c+1:
                # 리스트의 모든 곳을 탐색
                for i in range(N):
                    for j in range(M):
                        # info 리스트에서 .이 아닌 알파벳 문자 이면서 visited가 초기값이거나 c인 경우
                        if info[j][i] == alphabet[kind] and (visited[j][i] == c or visited[j][i] == -1):
                            visited[j][i] = c  # 초기값 변경을 위한 코드
                            # 상하좌우 증식 진행
                            for x, y in zip(dx, dy):
                                nx = j + x
                                ny = i + y
                                # 배지통의 범위를 넘지 않으면서 알파벳 문자가 아닌 .으로 구성된 경우
                                if 0 <= nx <= (M-1) and 0 <= ny <= (N-1) and info[nx][ny] == '.':
                                    info[nx][ny] = alphabet[kind]
                                    visited[nx][ny] = c+1
            else: continue
    return info





T = int(input())

# 알파벳 리스트 생성
alphabet = ['.', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# print(alphabet[26])

for tc in range(1, T+1):
    N, M = map(int, input().split())
    K = int(input())
    # K는 세균 종류의 수이므로, K값을 바탕으로 세균 종류 리스트 생성
    kinds = [v for v in range(1, K+1)]
    size = list(map(int, input().split()))
    info = [list(map(str, input().split())) for _ in range(M)]
    # print(info)
    result = lab(info, kinds, size)
    # 배지 데이터 출력 시 각 칸 사이에 공백이 있음에 유의
    print(f'#{tc}')
    for col in result:
        print(*col)
