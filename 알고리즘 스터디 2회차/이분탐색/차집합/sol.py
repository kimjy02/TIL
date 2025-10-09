N, M = map(int, input().split())
N_lst = list(map(int, input().split()))
M_lst = list(map(int, input().split()))

count = 0
answer_list = []

for check in range(len(N_lst)):
    for com in M_lst:
        if N_lst[check] == com:
            # count += 1
            # answer_list.append(check)
            break
    if

if count == 0:
    print(count)
else:
    print(count)
    print(*answer_list)