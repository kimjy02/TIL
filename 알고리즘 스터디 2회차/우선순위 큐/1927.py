import sys
import heapq
input = sys.stdin.readline

array = []

N = int(input())

for _ in range(N):
    x = int(input())
    if x != 0:  # 배열에 x값 추가
        heapq.heappush(array, x)
    else:  # 0이면 배열에서 가장 작은 값 출력
        if len(array) == 0:  # 빈 배열이라면 0 출력
            print(0)
        else:
            print(heapq.heappop(array))
