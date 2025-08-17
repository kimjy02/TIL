'''
    입력
        1. T : 테스트 케이스 수
        2. N : 디저트 카페가 모여있는 지역의 한 변의 길이 (4 <= N <= 20)
        3. 디저트 카페에서 팔고 있는 디저트 종류에 대한 정보 (1 <= info <= 100)

    출력
        - #{tc} {디저트를 가장 많이 먹을 때의 디저트 수}
'''

# import sys
# sys.stdin = open('sample_input.txt')

# 반시계 방향
dr = [+1, +1, -1, -1]
dc = [-1, +1, +1, -1]

def process(row, col, idx):
    nr = row + dr[idx]
    nc = col + dc[idx]
    if 0 <= nr <= N-1 and 0 <= nc <= N-1:
        if cafe[nr][nc] not in dessert:
            dessert.append(cafe[nr][nc])
            path.append([nr,nc])
            process(nr, nc, idx)
            # print(nr, nc)

        if idx+1 <= 3:
            process(nr, nc, idx+1)
                # print(nr, nc)
        else:
            dessert.pop()
            path.pop()

    else:
        return print(dessert, path)


    # for i in range(len(dr)):
    #     nr = row + dr[i]
    #     nc = col + dc[i]
    #     if 0 <= nr <= N-1 and 0 <= nc <= N-1:
    #         if cafe[nr][nc] not in dessert:
    #             dessert.append(cafe[nr][nc])
    #             path.append([nr,nc])
    #             # print(nr, nc)
    #             # print(dessert, path)
    #             process(nr, nc)
    #
    #     #     # else:
    #     #     #     dessert.pop()
    #     #     #     path.pop()
    #     #     #     return
    #     # else:
    #     #     return
    #
    # return dessert, path

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    # print(cafe)
    max_result = 0
    for row in range(0, N-2):
        for col in range(1, N-1):
            dessert = [cafe[row][col]]
            path = [[row,col]]
            process(row, col, 0)
            # max_result = max(max_result, len(path))
    # print(max_result)