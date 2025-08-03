# import sys
#
#
# sys.stdin = open("input.txt", 'r')
#
# N = sys.stdin.readline()



for t in range(10):
    side = int(input()) # 100
    # 정사각형 테이블 데이터
    data = [list(map(int, input().split())) for _ in range(side)]
    answer = 0 # 교착 상태 개수

    # 0부터 99까지 순회
    for i in range(side):
        # 1(N극)이 나오면 넣을 stack
        stack = []
        # 정사각형 테이블의 행 하나씩 순회
        for row in data:
            if row[i] == 1:
                stack.append(row[i])

            # 2(S극)이 나오고, stack이 비어있지 않은 경우
            elif (row[i] == 2) and stack:
                # 교착 상태 개수 +1
                answer += 1
                # stack 초기화
                stack = []

    print(f"#{t+1} {answer}")