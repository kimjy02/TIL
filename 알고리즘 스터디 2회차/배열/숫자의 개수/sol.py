A = int(input())
B = int(input())
C = int(input())
num_arrange = [0]*10
# print(num_arrange)


arrange = list(str(A * B * C))
# print(arrange)

for num in arrange:
    num_arrange[int(num)] += 1

for num in num_arrange:
    print(num)


