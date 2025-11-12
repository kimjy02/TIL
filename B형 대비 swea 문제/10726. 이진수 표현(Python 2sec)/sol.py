# 9739/10000

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    sum = 0
    for i in range(N):
        sum += 2**i
    comparison = list((bin(sum & M).split('0b'))[1].strip())
    print(comparison)
    if '0' in comparison:
        print(f'#{tc} OFF')
    else:
        print(f'#{tc} ON')
