N = int(input())
pos = []
neg = []
ones = 0
zero = 0

for _ in range(N):
    x = int(input())
    if x > 1:
        pos.append(x)
    elif x == 1:
        ones += 1
    elif x == 0:
        zero += 1
    else:
        neg.append(x)

pos.sort(reverse=True)  # 양수는 큰 수부터
neg.sort()              # 음수는 작은 수부터

total = 0

# 양수 처리
for i in range(0, len(pos)-1, 2):
    total += pos[i] * pos[i+1]
if len(pos) % 2:  # 하나 남으면 더함
    total += pos[-1]

# 음수 처리
for i in range(0, len(neg)-1, 2):
    total += neg[i] * neg[i+1]
if len(neg) % 2:  # 하나 남았는데
    if zero == 0: # 0이 없으면 그냥 더함
        total += neg[-1]

# 1 처리
total += ones

print(total)
