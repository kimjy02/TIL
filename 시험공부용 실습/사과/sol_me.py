import sys
sys.stdin = open('input.txt')


def search(info):
    start = [0, 0, '오른쪽']
    rotation = 0
    num = 1

    while num <= M:
        for j in range(1, N-1):
            for i in range(1, N-1):
                if info[j][i] == num:
                    if start[2] =='위':
                        if (j - start[0]) >= 0 and (i - start[1]) >= 0:
                            start = [j, i, '아래']
                            num += 1
                            rotation += 2

                        elif (j - start[0]) >= 0 and (i - start[1]) < 0:
                            start = [j, i, '왼쪽']
                            num += 1
                            rotation += 3

                        elif (j - start[0]) < 0 and (i - start[1]) >= 0:
                            start = [j, i, '오른쪽']
                            num += 1
                            rotation += 1

                        elif (j - start[0]) < 0 and (i - start[1]) < 0:
                            start = [j, i, '왼쪽']
                            num += 1
                            rotation += 3

                    elif start[2] == '아래':
                        if (j - start[0]) >= 0 and (i - start[1]) >= 0:
                            start = [j, i, '오른쪽']
                            num += 1
                            rotation += 3

                        elif (j - start[0]) >= 0 and (i - start[1]) < 0:
                            start = [j, i, '왼쪽']
                            num += 1
                            rotation += 1

                        elif (j - start[0]) < 0 and (i - start[1]) >= 0:
                            start = [j, i, '오른쪽']
                            num += 1
                            rotation += 3

                        elif (j - start[0]) < 0 and (i - start[1]) < 0:
                            start = [j, i, '위']
                            num += 1
                            rotation += 2


                    elif start[2] == '왼쪽':
                        if (j - start[0]) >= 0 and (i - start[1]) >= 0:
                            start = [j, i, '아래']
                            num += 1
                            rotation += 3

                        elif (j - start[0]) >= 0 and (i - start[1]) < 0:
                            start = [j, i, '아래']
                            num += 1
                            rotation += 3

                        elif (j - start[0]) < 0 and (i - start[1]) >= 0:
                            start = [j, i, '오른쪽']
                            num += 1
                            rotation += 2

                        elif (j - start[0]) < 0 and (i - start[1]) < 0:
                            start = [j, i, '위']
                            num += 1
                            rotation += 1

                    elif start[2] == '오른쪽':
                        if (j - start[0]) >= 0 and (i - start[1]) >= 0:
                            start = [j, i, '아래']
                            num += 1
                            rotation += 1


                        elif (j - start[0]) >= 0 and (i - start[1]) < 0:
                            start = [j, i, '왼쪽']
                            num += 1
                            rotation += 2

                        elif (j - start[0]) < 0 and (i - start[1]) >= 0:
                            start = [j, i, '위']
                            num += 1
                            rotation += 3

                        elif (j - start[0]) < 0 and (i - start[1]) < 0:
                            start = [j, i, '위']
                            num += 1
                            rotation += 3
    return rotation

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    M = 0
    for i in info:
        for j in i:
            if M < j:
                M = j
    # print(max_num)
    print(f'#{tc} {search(info)}')