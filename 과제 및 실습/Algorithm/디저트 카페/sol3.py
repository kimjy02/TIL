# 반시계 방향
dr = [+1, +1, -1, -1]   # 좌하, 우하, 우상, 좌상
dc = [ +1, -1, -1, +1 ]

def dfs(r, c, dir, turns, lens, sr, sc):
    # visited / dessert_set / max_result 는 바깥에서 초기화
    global max_result

    # 현재 위치에서: 0) 같은 방향으로 전진  1) 한 번 회전해서 전진
    for turn_once in (0, 1):
        ndir = (dir + turn_once) % 4
        nturns = turns + (1 if turn_once == 1 else 0)
        if nturns > 3:   # 회전은 최대 3번
            continue

        nr = r + dr[ndir]
        nc = c + dc[ndir]

        # 격자 밖이면 불가
        if not (0 <= nr < N and 0 <= nc < N):
            continue

        # 시작점으로 복귀하려는 한 칸이라면: 루프 완성 조건 체크
        if (nr, nc) == (sr, sc):
            # 마지막 변(ndir)은 지금 밟으면서 길이 1이 확보된다고 보고,
            # 나머지 3변이 이미 1칸 이상인지 확인(오프바이원 방지)
            if nturns == 3 and all(l > 0 for i, l in enumerate(lens) if i != ndir):
                max_result = max(max_result, len(dessert_set))
            continue

        # 중복 디저트 or 좌표 재방문이면 불가
        d = cafe[nr][nc]
        if (nr, nc) in visited or d in dessert_set:
            continue

        # 진입
        visited.add((nr, nc))
        dessert_set.add(d)
        lens[ndir] += 1

        dfs(nr, nc, ndir, nturns, lens, sr, sc)

        # 백트래킹
        lens[ndir] -= 1
        dessert_set.remove(d)
        visited.remove((nr, nc))

import sys
sys.stdin = open('sample_input.txt')
# ---- 메인 루프 ----
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    max_result = -1  # 경로 없으면 -1

    # 시작점은 가장자리 한 칸 더 여유를 두는 편이 안전 (0..N-3, 1..N-2)
    for sr in range(0, N - 2):
        for sc in range(1, N - 1):
            visited = {(sr, sc)}
            dessert_set = {cafe[sr][sc]}
            lens = [0, 0, 0, 0]  # 각 변 길이 카운트
            dfs(sr, sc, 0, 0, lens, sr, sc)

    print(f"#{tc} {max_result}")