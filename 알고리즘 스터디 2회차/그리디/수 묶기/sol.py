N = int(input())

plus = []
minus = []
zero = 0
one = 0
for _ in range(N):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num < 0 :
        minus.append(num)
    elif num == 1:
        one += 1
    else:
        zero += 1

# print(plus)
# print(minus)
# print(zero, one)

total = 0
plus.sort(reverse = True)
minus.sort()

if len(plus) == 1:
    total += plus[0]
else:
    if len(plus) % 2 == 0:
        for i in range(0, len(plus), 2):
            total += plus[i] * plus[i + 1]
    else:
        for i in range(0, len(plus)-1, 2):
            total += plus[i] * plus[i + 1]
        total += plus[-1]

if len(minus) == 1:
    if zero != 0:
        pass
    else:
        total += minus[0]
else:
    if len(minus) % 2 == 0 :
        for i in range(0, len(minus), 2):
            total += minus[i] * minus[i + 1]
    elif (len(minus) % 2 != 0 and zero != 0):
        for i in range(0, len(minus)-1, 2):
            total += minus[i] * minus[i + 1]
    else:
        for i in range(0, len(minus)-1, 2):
            total += minus[i] * minus[i + 1]
        total += minus[-1]

total += one
print(total)