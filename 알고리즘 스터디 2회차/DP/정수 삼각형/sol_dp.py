n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

memo = [[0]*len(triangle[i]) for i in range(n)]
# print(memo)

memo[0][0] = triangle[0][0]

for i in range(n-1):
    for j in range(len(triangle[i])):
        if memo[i+1][j] < memo[i][j]+triangle[i+1][j]:
            memo[i+1][j] = memo[i][j]+triangle[i+1][j]

        if memo[i+1][j+1] < memo[i][j]+triangle[i+1][j+1]:
            memo[i+1][j+1] = memo[i][j]+triangle[i+1][j+1]

        else : pass

print(max(memo[-1]))
