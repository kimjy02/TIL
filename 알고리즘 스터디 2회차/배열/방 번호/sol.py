room = list(map(int, input().strip()))
# print(room)

num_range = [0] * 9

for room_num in room:
    if room_num == 9:
        num_range[6] += 1
    else:
        num_range[room_num] += 1

# num_range[6] = num_range[6] // 2 + 1
if num_range[6] % 2 == 0:
    num_range[6] = num_range[6] // 2
else:
    num_range[6] = num_range[6] // 2 + 1
print(max(num_range))
