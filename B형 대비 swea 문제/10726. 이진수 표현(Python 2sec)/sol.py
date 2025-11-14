# 9739/10000

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    mask = (1 << N) - 1
    if (M & mask) == mask:  # 하위 N비트가 전부 1인가?
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')

