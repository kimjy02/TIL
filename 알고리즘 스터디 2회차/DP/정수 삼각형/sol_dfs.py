def path(lst, distance, i, j):
    global max_value
    # print(i, j)
    distance += lst[i][j]
    if i == (n - 1):
        # print(i, j, distance)
        if distance > max_value:
            max_value = distance
        return

    for k in range(2):
        # print(i, j, distance)
        path(lst, distance, i+1, j+k)
        # distance -= lst[i+1][j+k]
        # print(i, j, distance)


n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

max_value = 0
distance = 0
# print(triangle)
path(triangle, distance, 0, 0)
print(max_value)

