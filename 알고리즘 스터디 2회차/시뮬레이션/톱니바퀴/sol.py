# rotate(1) : 마지막 원소를 맨 앞으로 / rotate(-1) : 첫번째 원소를 마지막으로
from collections import deque

def rotate_function(position, rotate):
    if position != 3 and cogwheels[position][2] != cogwheels[position + 1][-2]:
        cogwheels[position+1].rotate(-rotate)

    if position != 0 and cogwheels[position][-2] != cogwheels[position - 1][2]:
        cogwheels[position-1].rotate(-rotate)

    cogwheels[position].rotate(rotate)

cogwheels = []
for _ in range(4):
    cogwheels.append(deque(map(int, input().strip())))
# print(cogwheels)
rotate_count = int(input())

rotate_method = [list(map(int, input().split())) for _ in range(rotate_count)]

for i in range(rotate_count):
    position, rotate = rotate_method[i]
    rotate_function(position-1, rotate)

for i in range(4):
    print(cogwheels[i])
score = 0
for i in range(4):
    if cogwheels[i][0] == 0:
        pass
    else:
        score += 2**i

print(score)