import sys
input = sys.stdin.readline

K, L = map(int, input().split())
waiting = []
for _ in range(L):
    waiting.append(input().strip())

def keep_last_occurrences_list(arr):
    # 1) 각 값의 '마지막 인덱스' 기록
    last = {}
    for i, v in enumerate(arr):
        last[v] = i
    #     print(f'i : {i}, v : {v}')
    # print(last)

    # 2) 마지막 인덱스인 것만 남겨 새 리스트 구성
    out = []
    for i, v in enumerate(arr):
        if i == last[v]:
            out.append(v)
    return out

new_waiting = keep_last_occurrences_list(waiting)

for s in new_waiting[:K]:
    print(s)




# from collections import Counter

# waiting_count = Counter(waiting)
# # print(waiting_count.keys())

# i = 0

# while i <= len(waiting_count):
#     if waiting_count != 1:
#         waiting.remove(i[0])
#         waiting_count.items[1] -= 1
#     else:
#         i += 1

# # for i in waiting_count.items():
# #     # print(i[0])
# #     if i[1] != 1:
# #         while i[0] in waiting:
# #             waiting.remove(i[0])

# print(waiting)

# # for i in range(K):
# #     print(wa[i])