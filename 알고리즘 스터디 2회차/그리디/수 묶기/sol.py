from collections import deque

N = int(input())
lst = deque()
for _ in range(N):
    lst.append(int(input()))

total = 0
while lst:
    num = lst.popleft()
    plus_check = []
    minus_check = []
    if num > 0:
        if lst[0] <= 0:
            pass
        else:
            plus_check.append(num)
            if len(plus_check) != 1`:
                if len(plus_check) == 3:
                    if plus_check[0] >= plus_check[2]:
                        total += plus_check[0] * plus_check[1]
                        plus_check = [plus_check[2]]
                    else:
                        total += plus_check[0]
                        total += plus_check[1] * plus_check[2]
                        plus_check = []
