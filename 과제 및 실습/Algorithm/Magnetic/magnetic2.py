from collections import deque

for t in range(10):
    N = int(input())  # 보통 N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)]  # N x N 행렬 입력

    total = 0
    for col in range(N):  # 열 단위로 교착 상태 탐색
        queue = deque()

        # 이 열의 모든 행을 위에서 아래로 확인
        for row in range(N):
            val = matrix[row][col]
            if val == 1 or val == 2:
                queue.append(val)

        # 앞에 있는 2 제거
        while queue and queue[0] == 2:
            queue.popleft()

        # 뒤에 있는 1 제거
        while queue and queue[-1] == 1:
            queue.pop()

        # 교착 상태 개수 세기 (1 → 2 패턴)
        cnt = 0
        for i in range(len(queue) - 1):
            if queue[i] == 1 and queue[i + 1] == 2:
                cnt += 1

        total += cnt

    print(f"#{t+1} {total}")
