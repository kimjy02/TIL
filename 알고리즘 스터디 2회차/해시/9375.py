import sys
import math
input = sys.stdin.readline

T = int(input())  # 테스트케이스 수


for _ in range(T):
    n = int(input())
    dict = {}
    for _ in range(n):
        clothes, kind = map(str, input().split())
        if kind not in dict:
            dict[kind] = 0
        dict[kind] += 1

    kind_cnt = list(dict.values())
    # 예 : [2, 3, 4]일 때, 
    # 2에 대해서 <2개 중 하나만 고른다, 둘 다 고르지 않는다>(2+1)
    # 3에 대해서 <3개 중 하나만 고른다, 둘 다 고르지 않는다>(3+1)
    # 4에 대해서 <4개 중 하나만 고른다, 둘 다 고르지 않는다>(4+1)
    # ∴ 3 X 4 X 5 , 근데 2 3 4 모두 고르지 않게 되는 경우는 제외해야 하므로 -1
    kind_cnt = list(map(lambda x: x + 1, kind_cnt))
    cnt = math.prod(kind_cnt) - 1

    print(cnt)
    # print(type(dict.values()))
    # print(dict)
