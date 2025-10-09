N, M = map(int, input().split())

tree = list(map(int, input().split()))

tree.sort(reverse=True)

for t in range(1, len(tree)):
    pieces = 0
    for a in tree[:t+1]:
        pieces += a-tree[t]

    if pieces == M :
        print(tree[t])
        break
    elif pieces < M :
        pass
    else :
        retree = tree[:t]
        # print(retree)
        # print(pieces)
        m = 0
        min_value = min(retree)
        for r in retree:
            m += r - min_value
        M -= m
        print(min_value - M // len(retree))
        break


# lo, hi = 1, tree[0]
# ans = 0
#
# while lo <= hi:
#     mid = (lo + hi) // 2
#     # print(f'lo : {lo}, hi : {hi}, mid : {mid}')
#     pieces = 0
#     for x in arr:
#         pieces += x // mid
#         # print(f'pieces : {pieces}')
#         if pieces >= M:
#             break
#
#     if pieces >= M:
#         ans = mid
#         lo = mid + 1
#     else:
#         hi = mid - 1
#
# print(ans)
