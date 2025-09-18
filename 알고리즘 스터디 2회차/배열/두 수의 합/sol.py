n = int(input())
a = list(map(int, input().split()))
x = int(input())
count = 0
# for num in (itertools.combinations(a,2)):
#     if sum(num) == x:
#         count += 1

# 투 포인터 방법
# a.sort()
# left, right = 0, n-1
# while left < right:
#     s = a[left]+a[right]
#     if s == x:
#         count += 1
#         left += 1
#         right -= 1
#     elif s < x :
#         left += 1
#     else:
#         right -= 1
#
# print(count)

# 1 2 3 5 7 9 10 11 12

# 집합 방법
seen = set()
for num in a:
    if x - num in seen:
        count += 1

    seen.add(num)
    # print(seen)

print(count)