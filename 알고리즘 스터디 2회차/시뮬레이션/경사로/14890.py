N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# print(grid)

count = 0
for row in grid:
    if len(set(row)) == 1:
        count += 1
    else :
        info = []
        i = 0
        while i <= N+1:
            if i+L <= (N+1):
                if len(row[i : i + L]) != 1:
                    i += 1
                    continue
                else:
                    if len(info) != 0:
                        if row[i] == info[-1] + 1 or row[i] == info[-1] - 1 or row[i] == info[-1]:
                            info.append(row[i])
                            i += L
                        else:
                            i += 1
                            continue
                    print(info)
                    i += 1
                    continue
            else:
                i += 1
                continue






                    
                
        
# lst = [1, 2, 3, 4, 5, 6]
# print(lst[3:7])
