import sys
sys.stdin = open('input.txt')

'''
입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고,
 그 다음 줄부터 T개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 
벌통들의 크기 N, 선택할 수 있는 벌통의 개수 M, 
꿀을 채취할 수 있는 최대 양 C가 차례로 주어진다.

그 다음 줄부터 N*N 개의 벌통에서 채취할 수 있는 꿀의 양에 대한 정보가 주어진다.
'''

def power_set(x, y, idx, acc, benefit):
    '''
        data[x][y] 부터 data[x][y+M-1] 까지의 값으로 이루어진 배열
        x: 시작 행 위치
        y: 시작 열 위치

        현재 확인 중인
        [1, 5, 8] 중에, 0번째를 선택한다, 안한다
                  중에, 1번째를 선택한다, 안한다
                  중에, 2번째를 선택한다, 안한다
        idx: 현재 선택할 대상 요소의 idx

        acc: 이때까지 누적해서 선택해 온, 꿀들의 개수 총합

         benefit: 가치 총합
    '''
    global max_value
    # 유망성 없는 대상
    if acc > C:
        return

    # 재귀의 기저 조건
    if idx == M:
        # 여기까지 왔다? 조사가 다 됐다...
        # 그럼 이제 뭐함?
        if max_value < benefit:
            max_value = benefit
        return

    # 유도 조건
    # x, y는 첫 조사 대상위치 이므로 그대로 유지
    # 왜냐면, data[x][y+idx] 형태로 다음 대상 탐색
    # 가치 총합도 더해주자.
    now_benefit = data[x][y+idx] ** 2
    power_set(x, y, idx + 1, acc + data[x][y + idx], benefit + now_benefit)
    # 이번 y + idx 번째 요소 사용하지 않겠다.
    power_set(x, y, idx + 1, acc, benefit)



T = int(input())
for tc in range(1, T+1):
    # 벌통 크기: N, 개수: M, 최대 양: C
    # 3 <= N <= 10, 1 <= M <= 5, N >= M, 10 <= C <= 30
    N, M, C = map(int, input().split())
    # 각 칸별 꿀의 양
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M, C, data)

    # 최종 결괏값
    result = 0      # 최소치로 초기화

    '''
        data[x][y] ~ data[x][y+M-1] 까지의 벌통을 채취
        모든 시작지점 (x, y) 좌표부터 전체 순회
    '''
    for x in range(N):
        for y in range(N-M+1):
            '''
            # print(data[x][y])   # 여기서부터 y+M-1까지가 한세트,
            # data[x][y] ~ data[x][y-M+1] 까지의 벌꿀의 양을 다 더하기만 하면되나?
            # 아니다. 최종 계산에는 제곱으로 합해야 하고,
            # 그 합이 C보다 크면 안된다.
            # 6 + 1 < C ? for문으로 순회하면되나? M번만큼?
            # 1, 8, 5 일때, < C가 7일때를 만족하는 상황을 보려면?
                # 1. 순열
                # 2. 부분집합
            '''
            max_value = 0  # A가 벌어들일 수 있는 최대치
            power_set(x, y, 0, 0, 0)
            A_max_value = max_value

            for k in range(x, N):
                for l in range(N-M+1):
                    # 같은 행인데,
                    # B가 선택을 시작할 곳이
                    # A가 마지막으로 선택한 값보다 작으면 무시
                    if k == x and l < y+M: continue
                    max_value = 0   # B도 똑같은거 해야함
                    power_set(k, l, 0, 0, 0)
                    B_max_value = max_value
                    result = max(A_max_value + B_max_value, result)

    print(f'#{tc} {result}')
