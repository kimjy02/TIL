'''
3
6 2
-1 4 3 0 6 1
4 1
1 2 4 5
4 2
-1 -2 -3 -4
'''

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    if K == N/2:
        print(f'#{tc} {sum(lst)}')
        continue

    sum_lst = []
    for l in range(len(lst)-K+1):
        sum_lst.append([sum(lst[l:l+K]), l, l+K-1])
    sum_lst.sort(reverse=True)
    # print(sum_lst)

    if K == 1:
        print(f'#{tc} {sum_lst[0][0] + sum_lst[1][0]}')
        continue
    last = len(sum_lst)
    max_value = -10000000
    for i in range(len(sum_lst)-1):
        for j in range(i+1, len(sum_lst)):
            if j >= last:
                continue
            
            if sum_lst[i][1] > sum_lst[j][1]:
                if sum_lst[i][1] <= sum_lst[j][2]:
                    continue
                else:
                    max_value = max(max_value, sum_lst[i][0] + sum_lst[j][0])
                    last = j
                    continue
            
            if sum_lst[i][1] < sum_lst[j][1] :
                if sum_lst[i][2] >= sum_lst[j][1]:
                    continue
                else:
                    max_value = max(max_value, sum_lst[i][0] + sum_lst[j][0])
                    last = j
                    continue
    
    print(f'#{tc} {max_value}')