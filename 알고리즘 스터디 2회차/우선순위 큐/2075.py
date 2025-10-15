import sys
import heapq
input = sys.stdin.readline

N = int(input())

h = []

for _ in range(N):
    for x in map(int, input().split()):
        # 각 원소 추가
        heapq.heappush(h, x)

        # N번째로 큰 수를 출력해야 되기에 N까지의 수를 저장
        if len(h) <= N:
            pass
        else:  # 리스트 길이가 N보다 커지면 그중 가장 작은 값 제거
            heapq.heappop(h)

# print(h)
print(heapq.heappop(h))


# 아래 방법으로 진행하려 함
# N이 최대 1500까지 가능하다보니 메모리 초과가 뜸
# 심지어 그걸 1차원 배열로 바꾸는 과정에서 메모리를 더 쓰는 듯
# lst = []

# for _ in range(N):
#     lst.append(list(map(int, input().split())))

# lst = sum(lst, [])

# # print(lst)

# lst.sort(reverse=True)

# print(lst[N-1])