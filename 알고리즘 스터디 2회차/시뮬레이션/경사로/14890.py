import sys
input = sys.stdin.readline

def check(road, L):
    N = len(road)
    used = [False] * N  # 경사로 설치 여부 기록

    for i in range(N - 1):
        diff = road[i+1] - road[i]

        # 1) 높이 같으면 통과
        if diff == 0:
            continue

        # 2) 오르막
        elif diff == 1:
            for j in range(i, i - L, -1):
                if j < 0 or road[j] != road[i] or used[j]:
                    return False
                used[j] = True

        # 3) 내리막
        elif diff == -1:
            for j in range(i + 1, i + L + 1):
                if j >= N or road[j] != road[i+1] or used[j]:
                    return False
                used[j] = True

        # 4) 높이 차이 2 이상이면 불가능
        else:
            return False

    return True


# -------------------------------
N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0

# 1️⃣ 행 검사
for i in range(N):
    if check(board[i], L):
        ans += 1

# 2️⃣ 열 검사
for j in range(N):
    col = [board[i][j] for i in range(N)]
    if check(col, L):
        ans += 1

print(ans)
