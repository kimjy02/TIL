T = int(input())  # T : 테스트 케이스 수

answer= []
def grid_function(i, j):
    answer.append(grid[i][j])
    if len(answer) == 7:
        print(answer)
    if i == 0 :
        i += 1
        grid_function(i, j)
        j += 1
        grid_function(i, j)
        if j != 0 :
            j -= 1
            grid_function(i, j)
    elif i == 3:
        i -= 1
        grid_function(i, j)
        j += 1
        grid_function(i, j)
        if j != 0:
            j -= 1
            grid_function(i, j)





grid = []
for i in range(4):
    lst = list(map(int, input().split()))
    grid.append(lst)

grid_function(0, 0)